import sounddevice as sd
import soundfile as sf
from config import METR_CLICK_PATH, METR_CLICK_UP_PATH, METR_BPM_MAX, METR_BPM_MIN


class Metronome:
    def __init__(self, bpm=85, beats_per_bar=4):
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
        if status:
            print(time, status)
        self._current_idx += frames
        if self._current_idx - self._prev_idx >= self._wait and not self._play_click:
            # Time for next click
            self._update_click_vars()

        if self._play_click:
            # Check if it's time for next click
            # (fast tempo interrupts clicks mid-sound)
            if self._current_idx >= int(self._prev_idx + self._wait):
                self._update_click_vars()
                self._increase_beat_count()

            # Feed click to output buffer
            click_data = self._get_click_data(self._beat_counter, self._beats_per_bar)
            chunksize = min(len(click_data) - self._click_idx, frames)
            outdata[:chunksize] = click_data[self._click_idx:self._click_idx + chunksize]
            self._click_idx += chunksize

            if chunksize < frames:
                # Fill rest with silence
                outdata[chunksize:] = 0
                self._play_click = False
                self._increase_beat_count()
        else:
            # Fill entire output buffer with silence
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
        return bool(self._stream) and self._stream.active

    def start(self):
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
