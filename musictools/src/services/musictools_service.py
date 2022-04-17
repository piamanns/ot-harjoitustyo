from entities.tf_preset import TfPreset
from entities.tuning_fork import TuningFork
from entities.metronome import Metronome
from repositories.tf_preset_repository import tf_preset_repository


class MusictoolsService:
    def __init__(self):
        self._tfork = TuningFork()
        self._metronome = Metronome()

    def tfork_is_active(self):
        return self._tfork.is_active()

    def tfork_start(self):
        self._tfork.start()

    def tfork_stop(self):
        self._tfork.stop()

    def tfork_set_freq(self, freq: float):
        self._tfork.set_frequency(freq)

    def tfork_get_presets(self):
        return tf_preset_repository.get_all()

    def tfork_save_preset(self, freq: float, label: str):
        preset = TfPreset(freq, label)
        tf_preset_repository.save(preset)

    def tfork_delete_preset(self, preset_id: str):
        tf_preset_repository.delete(preset_id)

    def metronome_is_active(self):
        return self._metronome.is_active()

    def metronome_start(self):
        self._metronome.start()

    def metronome_stop(self):
        self._metronome.stop()

    def metronome_get_bpm(self):
        return self._metronome.get_bpm()

    def metronome_set_bpm(self, bpm: int):
        self._metronome.set_bpm(bpm)

mt_service = MusictoolsService()
