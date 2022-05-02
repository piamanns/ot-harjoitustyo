from database_connection import get_database_connection
from entities.tf_preset import TfPreset


class TfPresetRepository:
    """The class responsible for database operations regarding tuning fork presets.
    """

    def __init__(self, connection):
        """The class constructor.

        Args:
            connection: The Connection-object representing the database.
        """

        self._connection = connection
        #self.__tf_presets = [(440, "A"), (293.66, "D"),
                             #(196, "G"), (659.25, "E"), (466.16, "Bb")]
    def get_all(self):
        """Gets all saved tuning fork presets

        Returns:
            A list of TfPreset-objects.
        """

        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM tf_presets")

        rows = cursor.fetchall()
        return list(map(self._parse_preset, rows))

    def _parse_preset(self, row):
        """Helper function for parsing preset data

        Args:
            row: An instance of the class sqlite3.Row with data for a single preset.

        Returns:
            A TfPreset-object.
        """

        return TfPreset(row["freq"], row["label"], row["id"]) if row else None

    def save(self, preset: TfPreset):
        """Saves a preset for the Tuning Fork.

        Args:
            preset: The preset to be saved as a TfPreset-object.

        Returns:
            The saved preset as a TfPreset-object, now with
            the created preset-id.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "INSERT INTO tf_presets (freq, label) VALUES (:freq, :label)",
            {"freq": preset.freq, "label": preset.label}
        )
        preset.id = cursor.lastrowid
        self._connection.commit()
        return preset

    def delete(self, preset_id: str):
        """Deletes the tuning fork preset with the given id.

        Args:
            preset_id: The id of the preset to be deleted as a string.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "DELETE FROM tf_presets WHERE id=:id",
            {"id": preset_id}
        )

        self._connection.commit()

    def delete_all(self):
        """Deletes all tuning fork presets.
        """

        cursor = self._connection.cursor()

        cursor.execute("DELETE from tf_presets")

tf_preset_repository = TfPresetRepository(get_database_connection())
