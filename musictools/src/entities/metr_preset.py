

class MetrPreset:
    """Class describing saved presets for the metronome tool.
    """

    def __init__(self, bpm: int, beats_per_bar=1, label="", preset_id=None):
        """The class constructor.

        Args:
            bpm: An integer describing the beats per minute-value.
            beats_per_bar: The beats per bar-value as an integer. Defaults to 1.
            label: The label for the preset as a string. Defaults to "".
            preset_id: An integer serving as a unique identifer for the preset.
                       Defaults to None.
        """

        self.bpm = bpm
        self.beats_per_bar = beats_per_bar
        self.id = preset_id
        self.label = label

    def __str__(self):
        return f"{str(self.bpm)} bpm ({self.label})"

    def get_value(self):
        """Returns the numeral values stored in the preset

        Returns:
            The bpm and beats per bar values as a tuple
        """

        return (self.bpm, self.beats_per_bar)

    def get_label(self):
        """Gets the label stored in the preset.

        Returns:
          The preset's label as a string.
        """

        return self.label
