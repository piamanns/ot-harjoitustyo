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
            print(status)
        t = (self._start_idx + np.arange(frames)) / self._sample_rate
        t = t.reshape(-1, 1)
        outdata[:] = np.sin(2 * np.pi * self._frequency * t)
        self._start_idx += frames

    def start(self):
        self._stream = sd.OutputStream(channels=1, callback=self._callback, samplerate=44100)
        self._stream.start()

    def stop(self):
        self._stream.stop()
        self._start_idx = 0

    def is_active(self):
        return self._stream and self._stream.active

    def set_frequency(self, freq: float):
        self._frequency = float(freq)

    def get_frequency(self):
        return self._frequency
