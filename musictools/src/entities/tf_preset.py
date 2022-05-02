

class TfPreset:
    def __init__(self, freq: float, label: str, preset_id=None):
        self.id = preset_id
        self.freq = freq
        self.label = label

    def __str__(self):
        return f"{str(self.freq)} Hz ({self.label})"

    def get_value(self):
        return self.freq

    def get_label(self):
        return self.label
