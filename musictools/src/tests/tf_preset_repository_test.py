import unittest
from repositories.tf_preset_repository import tf_preset_repository
from entities.tf_preset import TfPreset


class TestTfPresetRepository(unittest.TestCase):
    def setUp(self):
        tf_preset_repository.delete_all()
        self.preset_a = TfPreset(440, "A4")
        self.preset_b = TfPreset(466.16, "B4")
        self.preset_c = TfPreset(261.63, "C4")

    def test_saving_first_preset_works(self):
        tf_preset_repository.save(self.preset_a)
        presets = tf_preset_repository.get_all()

        self.assertEqual(len(presets), 1)
        self.assertEqual(presets[0].freq, self.preset_a.freq)
        self.assertEqual(presets[0].label, self.preset_a.label)

    def test_saving_preset_when_some_already_exist_works(self):
        tf_preset_repository.save(self.preset_a)
        tf_preset_repository.save(self.preset_b)
        tf_preset_repository.save(self.preset_c)
        presets = tf_preset_repository.get_all()

        self.assertEqual(len(presets), 3)
        self.assertEqual(presets[2].freq, self.preset_c.freq)
        self.assertEqual(presets[2].label, self.preset_c.label)

    def test_get_all_returns_all_saved_presets(self):
        tf_preset_repository.save(self.preset_a)
        tf_preset_repository.save(self.preset_b)
        presets = tf_preset_repository.get_all()

        self.assertEqual(len(presets), 2)
        self.assertEqual(presets[0].freq, self.preset_a.freq)
        self.assertEqual(presets[0].label, self.preset_a.label)
        self.assertEqual(presets[1].freq, self.preset_b.freq)
        self.assertEqual(presets[1].label, self.preset_b.label)

    def test_deleting_preset_removes_preset(self):
        tf_preset_repository.save(self.preset_a)
        tf_preset_repository.save(self.preset_b)
        tf_preset_repository.delete(self.preset_a.id)
        presets = tf_preset_repository.get_all()

        self.assertEqual(len(presets), 1)
        self.assertEqual(presets[0].freq, self.preset_b.freq)
        self.assertEqual(presets[0].label, self.preset_b.label)
    
    def test_updating_preset_changes_values_correctly(self):
        saved_preset = tf_preset_repository.save(self.preset_a)
        new_freq = 659.25
        new_label = "E5"
        saved_preset.freq = new_freq
        saved_preset.label = new_label

        updated_preset = tf_preset_repository.update(saved_preset)
        self.assertEqual(updated_preset.freq, new_freq)
        self.assertEqual(updated_preset.label, new_label)
