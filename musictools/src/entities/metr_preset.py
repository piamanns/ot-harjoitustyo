

class MetrPreset:
    def __init__(self, bpm: int, beats_per_bar=1, preset_id=None, label=""):
        self.bpm = bpm
        self.beats_per_bar = beats_per_bar
        self.id = preset_id
        self.label = label

    def __str__(self):
        return f"{str(self.bpm)} bpm ({self.beats_per_bar}-beat)"

    def get_value(self):
        return (self.bpm, self.beats_per_bar)

    def get_label(self):
        return self.label
