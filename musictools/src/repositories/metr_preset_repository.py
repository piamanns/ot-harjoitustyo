from database_connection import get_database_connection
from entities.metr_preset import MetrPreset


class MetrPresetRepository:
    """The class responsible for database operations regarding metronome presets.
    """

    def __init__(self, connection):
        """The class constructor.

        Args:
            connection: The Connection-object representing the database.
        """

        self._connection = connection

    def get_all(self):
        """Gets all saved metronome presets

        Returns:
            A list of MetrPreset-objects.
        """

        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM metr_presets")

        rows = cursor.fetchall()
        return list(map(self._parse_preset, rows))

    def _parse_preset(self, row):
        """Helper function for parsing preset data.

        Args:
            row: An instance of the class sqlite3.Row with data for a single preset.

        Returns:
            A MetrPreset-object.
        """

        return MetrPreset(row["bpm"], row["bpbar"], row["label"], row["id"]) if row else None

    def save(self, preset):
        """Saves a preset for the Metronome.

        Args:
            preset: The preset to be saved as a MetrPreset-object.

        Returns:
            The saved preset as a MetrPreset-object, now with
            the created preset-id.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "INSERT INTO metr_presets (bpm, bpbar, label) VALUES (:bpm, :bpbar, :label)",
            {"bpm": preset.bpm, "bpbar": preset.beats_per_bar, "label": preset.label}
        )
        preset.id = cursor.lastrowid
        self._connection.commit()
        return preset

    def delete(self, preset_id):
        """Deletes the metronome preset with the given id.

        Args:
            preset_id: The id of the preset to be deleted as a string.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "DELETE FROM metr_presets WHERE id=:id",
            {"id": preset_id}
        )

        self._connection.commit()

    def update(self, preset):
        """Updates a saved preset for the metronome.

        Args:
            preset: The preset to be updated as MetrPreset-object.

        Returns:
            The updated preset as a MetrPreset-object.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "UPDATE metr_presets SET bpm=:bpm, bpbar=:bpbar, label=:label WHERE id=:id",
            {"bpm": preset.bpm, "bpbar": preset.beats_per_bar, "label": preset.label,
            "id":preset.id}
        )

        self._connection.commit()
        return preset

    def delete_all(self):
        """Deletes all metronome presets.
        """

        cursor = self._connection.cursor()

        cursor.execute("DELETE from metr_presets")

metr_preset_repository = MetrPresetRepository(get_database_connection())
