from database_connection import get_database_connection
from entities.tf_preset import TfPreset


class TfPresetRepository:
    def __init__(self, connection):
        self._connection = connection
        #self.__tf_presets = [(440, "A"), (293.66, "D"),
                             #(196, "G"), (659.25, "E"), (466.16, "Bb")]
    def get_all(self):
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM tf_presets")

        rows = cursor.fetchall()
        return list(map(self._parse_preset, rows))

    def _parse_preset(self, row):
        return TfPreset(row["freq"], row["label"], row["id"]) if row else None

    def save(self, preset: TfPreset):
        cursor = self._connection.cursor()

        cursor.execute(
            "INSERT INTO tf_presets (freq, label) VALUES (:freq, :label)",
            {"freq": preset.freq, "label": preset.label}
        )
        preset.id = cursor.lastrowid
        self._connection.commit()
        return preset

    def delete(self, preset_id: str):
        cursor = self._connection.cursor()

        cursor.execute(
            "DELETE FROM tf_presets WHERE id=:id",
            {"id": preset_id}
        )

        self._connection.commit()

    def delete_all(self):
        cursor = self._connection.cursor()

        cursor.execute("DELETE from tf_presets")

tf_preset_repository = TfPresetRepository(get_database_connection())
