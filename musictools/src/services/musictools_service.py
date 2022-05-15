from entities.tf_preset import TfPreset
from entities.metr_preset import MetrPreset
from entities.tuning_fork import TuningFork
from entities.metronome import Metronome
from repositories.tf_preset_repository import(
    tf_preset_repository as default_tf_preset_repository
)
from repositories.metr_preset_repository import(
    metr_preset_repository as default_metr_preset_repository
)


class MusictoolsService:
    """The class responsible for the app logic.
    """

    def __init__(self, tf_preset_repository=default_tf_preset_repository,
                 metr_preset_repository=default_metr_preset_repository):
        """The class constructor.

        Args:
            tf_preset_repository: An object with the methods of
                                  the TfPresetRepository class.
                                  Defaults to default_tf_preset_repository.
            metr_preset_repository: A object with the methods of
                                    the MetrPresetRepository class.
                                    Defaults to default_metr_preset_repository.
        """

        self._tfork = TuningFork()
        self._metronome = Metronome()
        self._tf_preset_repository = tf_preset_repository
        self._metr_preset_repository = metr_preset_repository
        self._tfork_active_preset_id = None
        self._metr_active_preset_id = None

    def tfork_is_active(self):
        """Returns the playing status of the tuning fork.

        Returns:
            True if the tuning sound is playing, otherwise False.
        """

        return self._tfork.is_active()

    def tfork_start(self):
        """Starts the tuning fork sound.
        """

        self._tfork.start()

    def tfork_stop(self):
        """Stops the tuning fork sound.
        """

        self._tfork.stop()

    def tfork_get_freq(self):
        """Returns the current frequency value of the tuning fork as a float.
        """

        return self._tfork.get_frequency()

    def tfork_set_freq(self, freq: float):
        """Sets the tuning fork frequency.

        Args:
            freq: The frequency as a float.

        Returns:
            The new frequency of the tuning fork as a float if the setting operation
            was successful, otherwise None.
        """

        return self._tfork.set_frequency(freq)

    def tfork_validate_freq(self, freq: float):
        """Validates the given frequency

        Args:
            freq: The frequency as a float.

        Returns:
            The validated frequency as a float; None if the frequency
            was invalid.
        """

        return self._tfork.validate_frequency(freq)

    def tfork_get_presets(self):
        """Returns the saved presets for the tuning fork.

        Returns:
            A list of TfPreset-objects.
        """

        return self._tf_preset_repository.get_all()

    def tfork_save_preset(self, freq: float):
        """Saves a preset for the tuning fork

        The frequency is validated before saving.
        A label for the preset consisting of the note name
        corresponding to the frequency is generated automatically.

        Args:
            freq: The frequency to be saved as a float.

        Returns:
            The saved preset as a TfPreset object if the save operation was successful,
            otherwise None.
        """

        freq = self.tfork_validate_freq(freq)
        if freq:
            label = self.tfork_get_note_name(freq)
            return self._tf_preset_repository.save(TfPreset(freq, label))
        return None

    def tfork_delete_preset(self, preset_id: str):
        """Deletes the tuning fork preset with the given id.

        Args:
            preset_id: The id of the preset as a string.
        """

        self._tf_preset_repository.delete(preset_id)

    def tfork_update_preset(self, freq: float, preset_id: int):
        """Updates the values stored in a tuning fork preset.

        Args:
            freq: The new frequency as a float.
            preset_id: The id of the preset to update as an integerl

        Returns:
          The updated preset as a TfPreset-object if the operation was succesful,
          otherwise None.
        """

        freq = self.tfork_validate_freq(freq)
        if freq:
            label = self.tfork_get_note_name(freq)
            preset = TfPreset(freq, label, preset_id)
            return self._tf_preset_repository.update(preset)
        return None

    def tfork_get_note_name(self, freq: float):
        """Returns the note name corresponding to the frequency.

        Args:
            freq: The frequency as a float.

        Returns:
            A string with the note name in scientific pitch notation.
        """

        return self._tfork.get_note_name(freq)

    def tfork_set_active_preset(self, preset_id: int):
        """Sets the active tuning fork preset

        Args:
            preset_id: The id corresponding to the currently selected preset
                      as an integer.
        """

        self._tfork_active_preset_id = preset_id

    def tfork_get_active_preset(self):
        """ Returns the id of the active tuning fork preset

        Returns:
          An integer correspoinding to the id-number of the currently
          selected tuning fork preset.
        """

        return self._tfork_active_preset_id

    def metr_is_active(self):
        """Returns the ticking status of the metronome.

        Returns:
            True if the metronome is ticking, otherwise False.
        """

        return self._metronome.is_active()

    def metr_start(self):
        """Starts the metronome.
        """

        self._metronome.start()

    def metr_stop(self):
        """Stops the metronome.
        """

        self._metronome.stop()

    def metr_get_bpm(self):
        """Returns the current bpm value of the metronome as an int.
        """

        return self._metronome.get_bpm()

    def metr_set_bpm(self, bpm: int):
        """Sets the bpm value of the metronome.

        Args:
            bpm: The bpm as an integer.

        Returns:
            The new bpm value for the metronome as an integer if the setting
            operation was succesful, otherwise None.
        """

        return self._metronome.set_bpm(bpm)

    def metr_set_beats_per_bar(self, beats: int):
        """Set the beats per bar-value for the metronome

        Args:
            beats: The beats per bar as an integer.
        """

        self._metronome.set_beats_per_bar(beats)

    def metr_get_beats_per_bar(self):
        """Returns the current beats per bar value of the metronome as an integer.
        """

        return self._metronome.get_beats_per_bar()

    def metr_get_presets(self):
        """Gets the saved presets for the metronome.

        Returns:
            A list of MetrPreset-objects.
        """

        return self._metr_preset_repository.get_all()

    def metr_save_preset(self, bpm: int, beats_per_bar: int):
        """Saves a preset for the metronome.

        Creates a label for the preset to be saved
        from the beats per bar-value.

        Args:
            bpm: Beats per minute as an integer.
            beats_per_bar: Beats per bar as an integer.

        Returns:
            The saved preset as a MetrPreset-object if the saving operation
            was succesful, otherwise None.
        """

        bpm = self._metronome.validate_bpm(bpm)
        if bpm:
            label = f"{beats_per_bar}-beat"
            preset = MetrPreset(bpm, beats_per_bar, label)
            return self._metr_preset_repository.save(preset)
        return None

    def metr_delete_preset(self, preset_id: str):
        """Deletes the metronome preset with the given id

        Args:
            preset: The id of the preset to be deleted as a string.
        """

        self._metr_preset_repository.delete(preset_id)

    def metr_update_preset(self, bpm: int, beats_per_bar: int, preset_id: int):
        """Updates the values stored in a metronome preset

        Args:
            bpm: The new bpm value as an integer.
            beats_per_bar: The new beats per bar value as an integer.
            preset_id: The id corresponding to the preset to be updated as an integer.

        Returns:
            The updated preset as a MetrPreset-object if the operation was succesful,
            otherwise None.
        """

        bpm = self._metronome.validate_bpm(bpm)
        if bpm:
            label = f"{beats_per_bar}-beat"
            preset = MetrPreset(bpm, beats_per_bar, label, preset_id)
            return self._metr_preset_repository.update(preset)
        return None

    def metr_set_active_preset(self, preset_id: int):
        """Sets the active metronome preset

        Args:
            preset_id: The id corresponding to the currently selected preset
                       as an integer.
        """

        self._metr_active_preset_id = preset_id

    def metr_get_active_preset(self):
        """ Returns the id of the active metronome preset

        Returns:
          An integer corresponding to the id-number of the currently
          selected metronome preset.
        """

        return self._metr_active_preset_id

mt_service = MusictoolsService()
