import unittest
from services.musictools_service import MusictoolsService
from config import TF_BASE_A

class FakeTfPresetRepository:
    def __init__(self):
        self.presets = []

    def save(self, tf_preset):
        self.presets.append(tf_preset)
        return tf_preset
    
    def get_all(self):
        return self.presets

class TestMusictoolsService(unittest.TestCase):
    def setUp(self):
        self.mt_service = MusictoolsService(FakeTfPresetRepository())  

    def test_saving_tfork_preset_with_valid_frequency_works(self):
        saved_preset = self.mt_service.tfork_save_preset(int(TF_BASE_A))

        presets_length = len(self.mt_service.tfork_get_presets())
        self.assertEqual(presets_length, 1)

        self.assertEqual(saved_preset.freq, int(TF_BASE_A))
        self.assertEqual(saved_preset.label, "A4")

    def test_saving_tfork_preset_with_non_float_frequency_does_nothing_and_returns_none(self):
        saved_preset = self.mt_service.tfork_save_preset("foo")

        presets_length = len(self.mt_service.tfork_get_presets())
        self.assertEqual(presets_length, 0)

        self.assertEqual(saved_preset, None)
