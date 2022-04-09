from tuning_fork import TuningFork

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

mt_service = MusictoolsService()
