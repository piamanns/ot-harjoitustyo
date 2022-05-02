import math
import sounddevice as sd
import numpy as np
from config import TF_FREQ_MAX, TF_FREQ_MIN


class TuningFork:
    def __init__(self, frequency=440):
        self._frequency = frequency
        self._sample_rate = 44100
        self._stream = None
        self._start_idx = 0
        self._note_analyzer = NoteAnalyzer()

    def _callback(self, outdata, frames, time, status):
        if status:
            print(time, status)
        section = (self._start_idx + np.arange(frames)) / self._sample_rate
        section = section.reshape(-1, 1)
        outdata[:] = np.sin(2 * np.pi * self._frequency * section)
        self._start_idx += frames

    def start(self):
        self._stream = sd.OutputStream(
            channels=1, callback=self._callback, samplerate=self._sample_rate)
        self._stream.start()

    def stop(self):
        self._stream.stop()
        self._start_idx = 0

    def is_active(self):
        return bool(self._stream) and self._stream.active

    def validate_frequency(self, freq: float):
        try:
            freq = float(freq)
            if int(TF_FREQ_MIN) <= freq <= int(TF_FREQ_MAX):
                return freq
        except ValueError:
            pass
        return None

    def set_frequency(self, freq: float):
        new_freq = self.validate_frequency(freq)
        if new_freq:
            self._frequency = new_freq
            return self._frequency
        return None

    def get_frequency(self):
        return self._frequency

    def get_note_name(self, freq: float):
        return self._note_analyzer.get_note_name(freq)


class NoteAnalyzer:
    def __init__(self, base_a=440):
        self._base_freq = base_a
        self._base_octave = 4
        self._note_names = [
            "A", "A#/Bb", "B", "C", "C#/Db", "D",
            "D#/Eb", "E", "F", "F#/Gb", "G", "G#Ab"
        ]

    def _calc_half_steps(self, freq: float):
        half_steps = (math.log2(freq) - math.log2(440)) * 12
        return round(half_steps)

    def _get_note_name(self, half_steps: int):
        name = self._note_names[half_steps % 12]
        octave = self._get_octave(half_steps)
        return f"{name}{octave}"

    def _get_octave(self, half_steps: int):
        if half_steps > 2:
            return self._base_octave + 1 + (half_steps-3)//12
        if half_steps < -9:
            return self._base_octave + (half_steps+9)//12
        return self._base_octave

    def get_note_name(self, freq: float):
        half_steps = self._calc_half_steps(freq)
        return self._get_note_name(half_steps)
