

class TfPreset:
    """Class describing saved presets for the tuning fork tool.
    """

    def __init__(self, freq: float, label: str, preset_id=None):
        """Class constructor.

        Args:
            freq: The saved frequency as float
            label: The preset label as a string.
            preset_id: An integer constituting a unique id for the preset.
                       Defaults to None.
        """

        self.id = preset_id
        self.freq = freq
        self.label = label

    def __str__(self):
        return f"{str(self.freq)} Hz ({self.label})"

    def get_value(self):
        """Gets the frequency stored in the preset.

        Returns:
            The frequency as a float.
        """

        return self.freq

    def get_label(self):
        """Gets the label stored in the preset.

        Returns:
            The label as a string.
        """

        return self.label
