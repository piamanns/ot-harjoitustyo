import unittest
from entities.metronome import Metronome


class TestTuningFork(unittest.TestCase):
    def setUp(self):
        self.metronome = Metronome()
    
    def test_setting_metronome_bpm_updates_bpm_correctly(self):
        self.metronome.set_bpm(120)
        self.assertEqual(self.metronome.get_bpm(), 120)
    
    def test_metronome_loads_click_sound_when_initialized(self):
        self.assertGreater(len(self.metronome._click_data), 0)
    
    def test_metronome_is_active_returns_correct_value_when_metr_not_started(self):
        is_active = self.metronome.is_active()
        self.assertEqual(is_active, False)
    
    def test_metronome_is_active_returns_correct_value_when_metrwas_started(self):
        self.metronome.start()
        is_active = self.metronome.is_active()
        self.assertEqual(is_active, True)
        self.metronome.stop()
    
    def test_metronome_is_active_returns_correct_value_when_metr_was_stopped(self):
        self.metronome.start()
        self.metronome.stop()
        is_active = self.metronome.is_active()
        self.assertEqual(is_active, False)

    
