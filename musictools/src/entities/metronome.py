import sounddevice as sd
import soundfile as sf
from config import METR_CLICK_PATH, METR_CLICK_UP_PATH, METR_BPM_MAX, METR_BPM_MIN


class Metronome:
    def __init__(self, bpm=85, time_signature=(4, 4)):
        self._bpm = bpm
        self._wait = 0
        self._beats_per_bar = time_signature[0]
        self._beat_unit = time_signature[1]
        self._beat_counter = 0
        self._sample_rate = 44100
        self._stream = None
        self._start_idx = 0
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
            click_data = self._click_up_data if self._beat_counter == 1 \
                                                and self._beats_per_bar > 1 \
                                             else self._click_data
            chunksize = min(len(click_data) - self._click_idx, frames)
            outdata[:chunksize] = click_data[self._click_idx:self._click_idx + chunksize]
            self._click_idx += chunksize
            if chunksize < frames:
                outdata[chunksize:] = 0
                self._play_click = False
                self.increase_beat_count()
            # Check if it's time for next click
            # even if previous hasn't finished playing yet (fast tempo)
            elif self._start_idx - self._prev_idx >= self._wait:
                self._play_click = False
                self.increase_beat_count()
        else:
            # Fill output buffer with silence
            outdata.fill(0)

    def increase_beat_count(self):
        self._beat_counter += 1
        if self._beat_counter > self._beats_per_bar:
            self._beat_counter = 1

    def is_active(self):
        return bool(self._stream) and self._stream.active

    def start(self):
        self._init_click_vars()
        self._stream = sd.OutputStream(channels=self._click_data.shape[1], callback=self._callback,
                                       blocksize=256, samplerate=self._sample_rate)
        self._stream.start()

    def _init_click_vars(self):
        self._beat_counter = 1
        self._wait = 60/self._bpm * self._sample_rate
        self._start_idx = 0
        self._prev_idx = 0
        self._click_idx = 0
        # Play first click immediately:
        self._play_click = True

    def stop(self):
        self._stream.stop()

    def validate_bpm(self, bpm: int):
        try:
            bpm = int(bpm)
            if int(METR_BPM_MIN) <= bpm <= int(METR_BPM_MAX):
                return bpm
        except ValueError:
            pass
        return None

    def set_bpm(self, bpm: int):
        new_bpm = self.validate_bpm(bpm)
        if new_bpm:
            self._bpm = new_bpm
            self._init_click_vars()
            return self._bpm
        return None

    def get_bpm(self):
        return self._bpm

    def set_beats_per_bar(self, beats: int):
        self._beats_per_bar = beats

    def get_beats_per_bar(self):
        return self._beats_per_bar
