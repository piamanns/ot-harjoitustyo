import math
import threading
import sounddevice as sd
import numpy as np
from config import TF_BASE_A, TF_FREQ_MAX, TF_FREQ_MIN


class TuningFork:
    """Class describing a digital tuning fork.

    The tuning fork generates and plays a sine wave with the requested frequency
    using the sounddevice module (https://python-sounddevice.readthedocs.io/).
    """


    def __init__(self, frequency=TF_BASE_A, base_a=TF_BASE_A):
        """The class constructor.

        Args:
            frequency: The starting frequency of the tuning fork as a string.
                       Defaults to the environment variable TF_BASE_A.
            base_a: The frequency of the A above middle C used as
                    a fixed reference point for note name calculations.
                    Defaults to environment variable TF_BASE_A.
        """

        self._frequency = int(frequency)
        self._sample_rate = 44100
        self._stream = None
        self._start_idx = 0
        self._note_analyzer = NoteAnalyzer(int(base_a))
        self._is_playing = False
        self._timer = None
        self._clear_output = False

        self._init_stream()

    def _init_stream(self):
        self._stream = sd.OutputStream(
            channels=1, callback=self._callback, samplerate=self._sample_rate)

    def _callback(self, outdata, frames, time, status):
        """Callback function for the sounddevice output stream.

        Complete documentation available at https://python-sounddevice.readthedocs.io/.

        Args:
            outdata: The output buffer as a numpy.ndarray. The callback function
                    must always fill the entire output buffer with data.
            frames: An integer describing the number of frames to be processed by the callback
                    function. Equals the length of the output buffer.
            time: A CFFI structure with timestamps, expressed in seconds and synchronised
                  with the time of the associated stream.
                  time.currentTime() returns the time the callback was invoked.
            status: A CallbackFlags object with bit flags indicating input/output
                    underflows or overflows.
        """

        if status:
            print(time, status)
        section = (self._start_idx + np.arange(frames)) / self._sample_rate
        section = section.reshape(-1, 1)
        outdata[:] = np.sin(2 * np.pi * self._frequency * section)
        if self._clear_output:
            outdata[:] = np.zeros_like(outdata)

        self._start_idx += frames

    def start(self):
        """Starts the tuning sound.
        """

        if self._timer:
            self._timer.cancel()

        self._clear_output = False
        self._start_idx = 0
        if not self._stream.active:
            self._stream.start()
        self._is_playing = True

    def stop(self):
        """Stops the tuning sound.

        Stops the sound with a slight delay, to give
        the stream callback function time to fill the output buffer
        with silence. This prevents crunching sound
        when stopping stream.
        """

        self._is_playing = False
        self._clear_output = True
        self._timer = threading.Timer(1, self._delayed_stop)
        self._timer.start()

    def _delayed_stop(self):
        self._stream.stop()

    def is_active(self):
        """Returns a boolean describing the tuning sound status.

        Returns:
            True if the tuning sound is playing and False otherwise.
        """

        return self._is_playing

    def validate_frequency(self, freq: float):
        """Validates the frequency passed as an argument.

        The minimum and maximum values for the tuning fork frequency
        are set as environment variables.

        Args:
            freq: A float representing the frequency to be validated.

        Returns:
            The validated frequency as a float, or None if the frequency
            was invalid.
        """

        try:
            freq = float(freq)
            if int(TF_FREQ_MIN) <= freq <= int(TF_FREQ_MAX):
                return freq
        except ValueError:
            pass
        return None

    def set_frequency(self, freq: float):
        """Sets the frequency for the tuning fork

        Args:
            freq: A float describing the frequency.

        Returns:
            The new frequency of the tuning fork as a float if the setting operation
            was successful, otherwise None.
        """

        new_freq = self.validate_frequency(freq)
        if new_freq:
            self._frequency = new_freq
            return self._frequency
        return None

    def get_frequency(self):
        """Gets the current frequency of the tuning fork.

        Returns:
            The frequency as a float.
        """

        return self._frequency

    def get_note_name(self, freq: float):
        """Returns the note name for a frequency.

        Args:
            freq: The frequency as a float.

        Returns:
            A string containing the note name corresponding to the frequency.
            The note name is calculated using an equal tempered scale
            and encoded in Scientific Pitch Notation, where for example
            G#/Ab4 stands for G#/Ab in octave 4. The octave numbering
            starts from the lowest c on a grnd piano (C1). Middle c i C4.
        """

        return self._note_analyzer.get_note_name(freq)


class NoteAnalyzer:
    """Helper class for Tuning Fork that calculates note names.
    """

    def __init__(self, base_a=int(TF_BASE_A)):
        """The class constructor.

        Args:
            base_a: The frequency of the A above middle C used as a fixed base
                      for note name calculations. Defaults to the environment
                      variable TF_BASE_A.
        """

        self._base_freq = base_a
        self._base_octave = 4
        self._note_names = [
            "A", "A#/Bb", "B", "C", "C#/Db", "D",
            "D#/Eb", "E", "F", "F#/Gb", "G", "G#Ab"
        ]

    def _calc_half_steps(self, freq: float):
        """Calculates the frequency's distance to base A in half steps.

        Args:
            freq: The frequency as a float.

        Returns:
            The number of half steps as an integer.
        """

        half_steps = (math.log2(freq) - math.log2(self._base_freq)) * 12
        return round(half_steps)

    def _get_note_name(self, half_steps: int):
        """Returns the note name.

        Args:
            half_steps: An integer describing the distance to base A (A4) in half steps.

        Returns:
            A string with the note name in scientific pitch notation
            (note name followed by octave number).
        """

        name = self._note_names[half_steps % 12]
        octave = self._get_octave(half_steps)
        return f"{name}{octave}"

    def _get_octave(self, half_steps: int):
        """Returns the octave number for the note

        Args:
            half_steps: An integer describing the distance to base A (A4) in half steps.

        Returns:
            An integer describing the octave, relative to the middle octave 4.
        """

        if half_steps > 2:
            return self._base_octave + 1 + (half_steps-3)//12
        if half_steps < -9:
            return self._base_octave + (half_steps+9)//12
        return self._base_octave

    def get_note_name(self, freq: float):
        """Returns the note name for the given frequency

        Args:
            freq: The frequency as a float.

        Returns:
            A string with the note name in scientific pitch notation
            (note name followed by octave number).
        """

        half_steps = self._calc_half_steps(freq)
        return self._get_note_name(half_steps)
