import math
import itertools
import sounddevice as sd
import numpy as np


class TuningFork:
    def __init__(self):
        self._oscillator = self._get_sine_oscillator()
        self._stream = None

    def _get_sine_oscillator(self, frequency=440, sample_rate=44100):
        incr = (2 * math.pi * frequency) / sample_rate
        return (math.sin(value) for value in itertools.count(start=0, step=incr))

    def _get_samples(self, oscillator):
        return [int(next(oscillator) * 32767) for i in range(256)]
    
    def _callback(self, outdata, frames, time, status):
        if status:
            print(status)
        samples = self._get_samples(self._oscillator)
        outdata[:] = np.int16(samples).tobytes()
      
    def start(self):
        self._stream = sd.RawOutputStream(channels=1, callback=self._callback, dtype="int16", 
                                          blocksize=256, samplerate=44100)
        self._stream.start()
    
    def stop(self):
        self._stream.stop()
    
    def is_active(self):
        return self._stream and self._stream.active