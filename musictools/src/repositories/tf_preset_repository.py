from pathlib import Path
from config import TF_PRESETS_PATH
from entities.tf_preset import TfPreset


class TfPresetRepository:
    def __init__(self, tf_presets_path: str):
        self.__tf_presets_path = tf_presets_path
        #self.__tf_presets = [(440, "A"), (293.66, "D"),
                             #(196, "G"), (659.25, "E"), (466.16, "Bb")]
    def get_all(self):
        Path(self.__tf_presets_path).touch()
        return self.__read_presets()

    def save(self, tf_preset):
        presets = self.__read_presets()
        presets.append(tf_preset)
        self.__write_presets(presets)

    def delete(self, preset_id):
        presets = self.__read_presets()
        presets_updated = [preset for preset in presets if preset.id != preset_id]
        self.__write_presets(presets_updated)

    def delete_all(self):
        self.__write_presets([])

    def __read_presets(self):
        presets = []

        with open(self.__tf_presets_path, encoding="utf-8") as file:
            for row in file:
                row = row.strip()
                parts = row.split(";")
                preset_id = parts[0]
                freq = float(parts[1])
                label = parts[2]
                presets.append(TfPreset(freq, label, preset_id))

            return presets

    def __write_presets(self, presets):
        with open(self.__tf_presets_path, "w", encoding="utf-8") as file:
            for preset in presets:
                file.write(f"{preset.id};{preset.freq};{preset.label}\n")

tf_preset_repository = TfPresetRepository(TF_PRESETS_PATH)
