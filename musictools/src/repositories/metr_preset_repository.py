from pathlib import Path
from config import METR_PRESETS_PATH
from entities.metr_preset import MetrPreset


class MetrPresetRepository:
    def __init__(self, metr_presets_path: str):
        self.__metr_presets_path = metr_presets_path

    def get_all(self):
        return self.__read_presets()

    def save(self, metr_preset):
        presets = self.get_all()
        presets.append(metr_preset)
        self.__write_presets(presets)
        return metr_preset

    def delete(self, preset_id):
        presets = self.__read_presets()
        presets_updated = [preset for preset in presets if preset.id != preset_id]
        self.__write_presets(presets_updated)

    def __read_presets(self):
        Path(self.__metr_presets_path).touch()
        presets = []

        with open(self.__metr_presets_path, encoding="utf-8") as file:
            for row in file:
                row = row.strip()
                parts = row.split(";")
                preset_id = parts[0]
                bpm = int(parts[1])
                beats_per_bar = int(parts[2])
                beat_unit = int(parts[3])
                presets.append(MetrPreset(bpm, beats_per_bar, beat_unit, preset_id))

            return presets

    def __write_presets(self, presets):
        Path(self.__metr_presets_path).touch()
        with open(self.__metr_presets_path, "w", encoding="utf-8") as file:
            for preset in presets:
                file.write(
                    f"{preset.id};{preset.bpm};{preset.beats_per_bar};{preset.beat_unit}\n"
                )

metr_preset_repository = MetrPresetRepository(METR_PRESETS_PATH)
