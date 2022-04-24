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
    def __init__(self, tf_preset_repository=default_tf_preset_repository,
                 metr_preset_repository=default_metr_preset_repository):
        self._tfork = TuningFork()
        self._metronome = Metronome()
        self._tf_preset_repository = tf_preset_repository
        self._metr_preset_repository = metr_preset_repository

    def tfork_is_active(self):
        return self._tfork.is_active()

    def tfork_start(self):
        self._tfork.start()

    def tfork_stop(self):
        self._tfork.stop()

    def tfork_set_freq(self, freq: float):
        return self._tfork.set_frequency(freq)

    def tfork_validate_freq(self, freq: float):
        return self._tfork.validate_frequency(freq)

    def tfork_get_presets(self):
        return self._tf_preset_repository.get_all()

    def tfork_save_preset(self, freq: float, label: str):
        freq = self.tfork_validate_freq(freq)
        if freq:
            preset = TfPreset(freq, label)
            return self._tf_preset_repository.save(preset)
        return None

    def tfork_delete_preset(self, preset_id: str):
        self._tf_preset_repository.delete(preset_id)

    def metr_is_active(self):
        return self._metronome.is_active()

    def metr_start(self):
        self._metronome.start()

    def metr_stop(self):
        self._metronome.stop()

    def metr_get_bpm(self):
        return self._metronome.get_bpm()

    def metr_set_bpm(self, bpm: int):
        return self._metronome.set_bpm(bpm)

    def metr_set_beats_per_bar(self, beats: int):
        self._metronome.set_beats_per_bar(beats)

    def metr_get_beats_per_bar(self):
        return self._metronome.get_beats_per_bar()

    def metr_get_presets(self):
        return self._metr_preset_repository.get_all()

    def metr_save_preset(self, bpm: int, beats_per_bar: int, beat_unit: int):
        bpm = self._metronome.validate_bpm(bpm)
        if bpm:
            preset = MetrPreset(bpm, beats_per_bar, beat_unit)
            return self._metr_preset_repository.save(preset)
        return None

    def metr_delete_preset(self, preset_id: str):
        self._metr_preset_repository.delete(preset_id)

mt_service = MusictoolsService()
