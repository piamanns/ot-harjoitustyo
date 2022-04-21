import sounddevice as sd
import soundfile as sf
from config import METR_CLICK_PATH, METR_CLICK_UP_PATH, METR_BPM_MAX, METR_BPM_MIN


class Metronome:
    def __init__(self, bpm=60, time_signature=(4, 4)):
        self._bpm = bpm
        self._wait = 0
        self._beats_per_bar = time_signature[0]
        self._beat_unit = time_signature[1]
        self._sample_rate = 44100
        self._stream = None
        self._start_idx = 0
        self._prev_idx = 0
        self._click_idx = 0
        self._click_data = None
        self._click_up_data = None
        self._play_click = False
        self._click_counter = 0

        self._load_clicksound()

    def _load_clicksound(self):
        self._click_data, self._sample_rate = sf.read(METR_CLICK_PATH, always_2d=True)

    def _callback(self, outdata, frames, time, status):
        if status:
            print(time, status)
        self._start_idx += frames
        if self._start_idx - self._prev_idx >= self._wait and not self._play_click:
            # Time for next click
            self._prev_idx += self._wait
            self._click_idx = 0
            self._play_click = True

        if self._play_click:
            # Feed click to output buffer
            # TODO: Check if next click should start partly on top of previous
            # (for even better accuracy when tempo is fast)
            chunksize = min(len(self._click_data) - self._click_idx, frames)
            outdata[:chunksize] = self._click_data[self._click_idx:self._click_idx + chunksize]
            self._click_idx += chunksize
            if chunksize < frames:
                outdata[chunksize:] = 0
                self._play_click = False
            # Check if it's time for next click
            # even if previous hasn't finished playing yet (fast tempo)
            if self._start_idx - self._prev_idx >= self._wait:
                self._play_click = False
        else:
            # Fill output buffer with silence
            outdata.fill(0)

    def is_active(self):
        return bool(self._stream) and self._stream.active

    def start(self):
        self._init_click_vars()
        self._stream = sd.OutputStream(channels=self._click_data.shape[1], callback=self._callback,
                                       blocksize=256, samplerate=self._sample_rate)
        self._stream.start()

    def _init_click_vars(self):
        self._wait = 60/self._bpm * self._sample_rate
        self._start_idx = 0
        self._prev_idx = 0
        self._click_idx = 0
        self._click_counter = 0
        # Play first click immediately:
        self._play_click = True

    def stop(self):
        self._stream.stop()

    def set_bpm(self, bpm: int):
        try:
            new_bpm = int(bpm)
            if int(METR_BPM_MIN) <= new_bpm <= int(METR_BPM_MAX):
                self._bpm = new_bpm
                self._init_click_vars()
                return self._bpm
        except ValueError:
            pass
        return None

    def get_bpm(self):
        return self._bpm
