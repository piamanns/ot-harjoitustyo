import sounddevice as sd
import soundfile as sf
from config import METR_CLICK_PATH, METR_CLICK_UP_PATH, METR_BPM_MAX, METR_BPM_MIN


class Metronome:
    """Class describing a clicking metronome.

    The class utilizes the SoundFile audio library to read the click sound files
    from disk. (https://python-soundfile.readthedocs.io/en/0.10.3post1/).
    The metronome sound is output using the sounddevice module
    (https://python-sounddevice.readthedocs.io/).

    """

    def __init__(self, bpm=85, beats_per_bar=4):
        """The class constructor.

        Args:
            bpm: A starting value for the beats per minute-setting for the
                 metronome as an integer. Defaults to 85.
            beats_per_bar: An initial value for the beats per bar-setting for the
                           metronome as an integer. Defaults to 4.
        """

        self._bpm = bpm
        self._wait = 0
        self._beats_per_bar = beats_per_bar
        self._beat_counter = 0
        self._sample_rate = 44100
        self._stream = None
        self._current_idx = 0
        self._prev_idx = 0
        self._click_idx = 0
        self._click_data = None
        self._click_up_data = None
        self._play_click = False

        self._load_clicksounds()

    def _load_clicksounds(self):
        self._click_data, self._sample_rate = sf.read(METR_CLICK_PATH, always_2d=True)
        self._click_up_data, self._sample_rate = sf.read(METR_CLICK_UP_PATH, always_2d=True)

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
        self._current_idx += frames
        if self._current_idx - self._prev_idx >= self._wait and not self._play_click:
            # Time for the next click, set up the variables
            self._update_click_vars()

        if self._play_click:
            # Check if next click should interrupt previous (fast tempo)
            if self._current_idx >= int(self._prev_idx + self._wait):
                self._update_click_vars()
                self._increase_beat_count()

            # Feed click sound data to output buffer
            click_data = self._get_click_data(self._beat_counter, self._beats_per_bar)
            chunksize = min(len(click_data) - self._click_idx, frames)
            outdata[:chunksize] = click_data[self._click_idx:self._click_idx + chunksize]
            self._click_idx += chunksize

            if chunksize < frames:
                # Fill rest of output buffer with silence
                outdata[chunksize:] = 0
                self._play_click = False
                self._increase_beat_count()
        else:
            outdata.fill(0)

    def _update_click_vars(self):
        self._prev_idx += self._wait
        self._click_idx = 0
        self._play_click = True

    def _get_click_data(self, beat_count:int, beats_per_bar: int):
        if beat_count == 1 and beats_per_bar > 1:
            return self._click_up_data
        return self._click_data

    def _increase_beat_count(self):
        self._beat_counter += 1
        if self._beat_counter > self._beats_per_bar:
            self._beat_counter = 1

    def is_active(self):
        """Returns a boolean describing the metronome's status.

        Returns:
            True if the metrome is currently running and False otherwise.
        """

        return bool(self._stream) and self._stream.active

    def start(self):
        """Starts the metronome.
        """

        self._init_click_vars()
        self._stream = sd.OutputStream(channels=self._click_data.shape[1], callback=self._callback,
                                       blocksize=256, samplerate=self._sample_rate)
        self._stream.start()

    def _init_click_vars(self):
        self._beat_counter = 1
        self._wait = 60/self._bpm * self._sample_rate
        self._current_idx = 0
        self._prev_idx = 0
        self._click_idx = 0
        # Play first click immediately:
        self._play_click = True

    def stop(self):
        """Stops the metronome.
        """

        self._stream.stop()

    def validate_bpm(self, bpm: int):
        """Validates the given bpm-value.

        The minimum and maximum values for the metronome bpm-setting
        are given as environment variables.

        Args:
            bpm: An integer describing the bpm-value to be validated.

        Returns:
            Returns the validated bpm-value as an integer
            if the value was within limits, otherwise None.
        """

        try:
            bpm = int(bpm)
            if int(METR_BPM_MIN) <= bpm <= int(METR_BPM_MAX):
                return bpm
        except ValueError:
            pass
        return None

    def set_bpm(self, bpm: int):
        """Sets the bpm-value for the metronome.

        Args:
            bpm: The new beats per minute-value as an integer.

        Returns:
            The new bpm-value for the metronome if the setting operation
            was succesful, otherwise None.
        """

        new_bpm = self.validate_bpm(bpm)
        if new_bpm:
            self._bpm = new_bpm
            self._init_click_vars()
            return self._bpm
        return None

    def get_bpm(self):
        """Gets the current bpm-value for the metronome.

        Returns:
            The current beats per minute-value as an integer.
        """

        return self._bpm

    def set_beats_per_bar(self, beats: int):
        """Set the beats per bar-value for the metronome.

        Args:
            beats: An integer describing the new beats per bar-value.
        """

        self._beats_per_bar = beats

    def get_beats_per_bar(self):
        """Gets the current beats per bar-value

        Returns:
            The current beats per bar-setting for the metronome
            as an integer.
        """

        return self._beats_per_bar
