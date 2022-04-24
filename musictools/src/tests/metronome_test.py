import unittest
from entities.metronome import Metronome
from config import METR_BPM_MIN, METR_BPM_MAX


class TestTuningFork(unittest.TestCase):
    def setUp(self):
        self.metronome = Metronome()
    
    def test_setting_metronome_bpm_updates_bpm_correctly(self):
        self.metronome.set_bpm(120)
        self.assertEqual(self.metronome.get_bpm(), 120)
    
    def test_metronome_loads_some_click_sound_data_when_initialized(self):
        self.assertGreater(len(self.metronome._click_data), 1000)
    
    def test_setting_metronome_bpm_to_non_int_does_nothing_returns_None(self):
        self.metronome.set_bpm(100)
        bpm = self.metronome.set_bpm("abc")
        self.assertEqual(self.metronome.get_bpm(), 100)
        self.assertEqual(bpm, None)
    
    def test_setting_metronome_bpm_to_less_than_min_value_does_nothing_returns_None(self):
        self.metronome.set_bpm(100)
        bpm = self.metronome.set_bpm(int(METR_BPM_MIN)-1)
        self.assertEqual(self.metronome.get_bpm(), 100)
        self.assertEqual(bpm, None)
    
    def test_setting_metronome_bpm_to_more_than_max_value_does_nothing_returns_None(self):
        self.metronome.set_bpm(100)
        bpm = self.metronome.set_bpm(int(METR_BPM_MAX)+1)
        self.assertEqual(self.metronome.get_bpm(), 100)
        self.assertEqual(bpm, None)

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

    def test_setting_metronome_beats_per_bar_works(self):
        self.metronome.set_beats_per_bar(7)
        bpb = self.metronome.get_beats_per_bar()
        self.assertEqual(bpb, 7)

    
