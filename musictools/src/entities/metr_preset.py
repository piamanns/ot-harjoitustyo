

class MetrPreset:
    def __init__(self, bpm: int, beats_per_bar=1, beat_unit=4, preset_id=None):
        self.bpm = bpm
        self.beats_per_bar = beats_per_bar
        self.beat_unit = beat_unit
        self.id = preset_id

    def __str__(self):
        return f"{str(self.bpm)} bpm"

    def get_value(self):
        return self.bpm
