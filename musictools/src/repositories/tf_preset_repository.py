class TfPresetRepository:
    def __init__(self):
        self.__tf_presets = [(440, "A"), (293.66, "D"),
                             (196, "G"), (659.25, "E"), (466.16, "Bb")]

    def get_all(self):
        return self.__tf_presets

    def save(self, tf_preset):
        self.__tf_presets.append(tf_preset)


tf_preset_repository = TfPresetRepository()
