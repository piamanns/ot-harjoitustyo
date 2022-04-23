import uuid


class TfPreset:
    def __init__(self, freq: float, label: str, preset_id=None):
        self.freq = freq
        self.label = label
        self.id = preset_id or str(uuid.uuid4())

    def __str__(self):
        return str(self.freq)

    def get_value(self):
        return self.freq
