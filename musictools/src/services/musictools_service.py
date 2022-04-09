from tuning_fork import TuningFork
from repositories.tf_preset_repository import tf_preset_repository


class MusictoolsService:
    def __init__(self):
        self._tfork = TuningFork()

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

    def tfork_save_preset(self, preset):
        return tf_preset_repository.save(preset)


mt_service = MusictoolsService()
