from database_connection import get_database_connection
from entities.metr_preset import MetrPreset


class MetrPresetRepository:
    def __init__(self, connection):
        self._connection = connection

    def get_all(self):
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM metr_presets")

        rows = cursor.fetchall()
        return list(map(self._parse_preset, rows))

    def _parse_preset(self, row):
        return MetrPreset(row["bpm"], row["bpbar"], row["bunit"], row["id"]) if row else None

    def save(self, preset):
        cursor = self._connection.cursor()

        cursor.execute(
            "INSERT INTO metr_presets (bpm, bpbar, bunit) VALUES (:bpm, :bpbar, :bunit)",
            {"bpm": preset.bpm, "bpbar": preset.beats_per_bar,
            "bunit": preset.beat_unit}
        )
        preset.id = cursor.lastrowid
        self._connection.commit()
        return preset

    def delete(self, preset_id):
        cursor = self._connection.cursor()

        cursor.execute(
            "DELETE FROM metr_presets WHERE id=:id",
            {"id": preset_id}
        )

        self._connection.commit()

    def delete_all(self):
        cursor = self._connection.cursor()

        cursor.execute("DELETE from metr_presets")

metr_preset_repository = MetrPresetRepository(get_database_connection())
