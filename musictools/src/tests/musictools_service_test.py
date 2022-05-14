import unittest
from services.musictools_service import MusictoolsService
from config import METR_BEATS_MAX, METR_BEATS_MIN, METR_BPM_MAX, METR_BPM_MIN, TF_BASE_A

class FakeTfPresetRepository:
    def __init__(self):
        self.presets = []

    def save(self, tf_preset):
        self.presets.append(tf_preset)
        return tf_preset
    
    def update(self, tf_preset):
        self.presets = [tf_preset if preset.id == tf_preset.id \
                        else preset for preset in self.presets]
        return tf_preset

    def get_all(self):
        return self.presets


class FakeMetrPresetRepository:
    def __init__(self):
        self.presets = []

    def save(self, metr_preset):
        self.presets.append(metr_preset)
        return metr_preset
    
    def update(self, metr_preset):
        self.presets = [metr_preset if preset.id == metr_preset.id \
                        else preset for preset in self.presets]
        return metr_preset

    def get_all(self):
        return self.presets


class TestMusictoolsService(unittest.TestCase):
    def setUp(self):
        self.mt_service = MusictoolsService(FakeTfPresetRepository(), FakeMetrPresetRepository())  

    def test_saving_tfork_preset_with_valid_frequency_works(self):
        saved_preset = self.mt_service.tfork_save_preset(int(TF_BASE_A))

        presets_length = len(self.mt_service.tfork_get_presets())
        self.assertEqual(presets_length, 1)

        self.assertEqual(saved_preset.freq, int(TF_BASE_A))
        self.assertEqual(saved_preset.label, "A4")

    def test_saving_tfork_preset_with_non_float_frequency_does_nothing_and_returns_None(self):
        saved_preset = self.mt_service.tfork_save_preset("foo")

        presets_length = len(self.mt_service.tfork_get_presets())
        self.assertEqual(presets_length, 0)

        self.assertEqual(saved_preset, None)

    def test_updating_tfork_preset_with_valid_frequency_works_correctly(self):
        saved_preset = self.mt_service.tfork_save_preset(int(TF_BASE_A))
        new_freq = 659.25
        self.mt_service.tfork_update_preset(new_freq, saved_preset.id)
        
        updated_preset = self.mt_service.tfork_update_preset(new_freq, saved_preset.id)
        self.assertEqual(updated_preset.freq, new_freq)
        self.assertEqual(updated_preset.label, self.mt_service.tfork_get_note_name(new_freq))
        self.assertEqual(updated_preset.id, saved_preset.id)
    
    def test_updating_tfork_preset_with_non_float_frequency_does_nothing_and_returns_None(self):
        saved_preset = self.mt_service.tfork_save_preset(int(TF_BASE_A))
        new_freq = "foo"
        self.mt_service.tfork_update_preset(new_freq, saved_preset.id)
        
        updated_preset = self.mt_service.tfork_update_preset(new_freq, saved_preset.id)
        self.assertEqual(updated_preset, None)

    def test_saving_metr_preset_with_valid_bpm_value_works(self):
        saved_preset = self.mt_service.metr_save_preset(int(METR_BPM_MAX), int(METR_BEATS_MAX))

        presets_length = len(self.mt_service.metr_get_presets())
        self.assertEqual(presets_length, 1)

        self.assertEqual(saved_preset.bpm, int(METR_BPM_MAX))
        self.assertEqual(saved_preset.beats_per_bar, int(METR_BEATS_MAX))
        self.assertEqual(saved_preset.label, f"{METR_BEATS_MAX}-beat")
    
    def test_saving_metr_preset_with_non_integer_bpm_value_does_nothing_and_returns_None(self):
        saved_preset = self.mt_service.metr_save_preset("foo", int(METR_BEATS_MAX))

        presets_length = len(self.mt_service.metr_get_presets())
        self.assertEqual(presets_length, 0)

        self.assertEqual(saved_preset, None)

    def test_updating_metr_preset_with_valid_bpm_value_works(self):
        saved_preset = self.mt_service.metr_save_preset(int(METR_BPM_MIN), int(METR_BEATS_MIN))

        updated_preset = self.mt_service.metr_update_preset(
            int(METR_BPM_MAX),
            int(METR_BEATS_MAX),
            saved_preset.id
        )

        self.assertEqual(updated_preset.bpm, int(METR_BPM_MAX))
        self.assertEqual(updated_preset.beats_per_bar, int(METR_BEATS_MAX))
        self.assertEqual(updated_preset.label, f"{int(METR_BEATS_MAX)}-beat")
        self.assertEqual(updated_preset.id, saved_preset.id)

    def test_updating_tfork_preset_with_non_int_bpm_value_does_nothing_and_returns_None(self):
        saved_preset = self.mt_service.metr_save_preset(int(METR_BPM_MIN), int(METR_BEATS_MIN))

        updated_preset = self.mt_service.metr_update_preset(
            "foo",
            int(METR_BEATS_MAX),
            saved_preset.id
        )

        self.assertEqual(updated_preset, None)
