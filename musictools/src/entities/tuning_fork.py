import sounddevice as sd
import numpy as np


class TuningFork:
    def __init__(self, frequency=440):
        self._frequency = frequency
        self._sample_rate = 44100
        self._stream = None
        self._start_idx = 0

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
            if freq >= 20 and freq <= 8000:
               return freq
        except ValueError:
            pass
        return None

    def set_frequency(self, freq: float):
        new_freq = self.validate_frequency(freq)
        if new_freq:
            self._frequency = new_freq
            return self._frequency
        else:
            return None

    def get_frequency(self):
        return self._frequency
