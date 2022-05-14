import unittest
from repositories.metr_preset_repository import metr_preset_repository
from entities.metr_preset import MetrPreset

class TestTfPresetRepository(unittest.TestCase):
    def setUp(self):
        metr_preset_repository.delete_all()
        self.preset_60 = MetrPreset(60, 6)
        self.preset_120 = MetrPreset(120, 3)
        self.preset_180 = MetrPreset(180, 2)

    def test_saving_first_preset_works(self):
        metr_preset_repository.save(self.preset_120)
        presets = metr_preset_repository.get_all()
        self.assertEqual(len(presets), 1)
        self.assertEqual(presets[0].bpm, self.preset_120.bpm)
        self.assertEqual(presets[0].beats_per_bar, self.preset_120.beats_per_bar)
    
    def test_saving_preset_when_some_already_exist_works(self):
        metr_preset_repository.save(self.preset_120)
        metr_preset_repository.save(self.preset_180)
        metr_preset_repository.save(self.preset_60)
        presets = metr_preset_repository.get_all()

        self.assertEqual(len(presets), 3)
        self.assertEqual(presets[2].bpm, self.preset_60.bpm)
        self.assertEqual(presets[2].beats_per_bar, self.preset_60.beats_per_bar)

    def test_saving_preset_returns_preset(self):
        preset = metr_preset_repository.save(self.preset_180)
        self.assertEqual(preset.bpm, self.preset_180.bpm)
        self.assertEqual(preset.beats_per_bar, self.preset_180.beats_per_bar)
 
    def test_getting_all_presets_returns_empty_list_when_none_are_saved(self):
        presets = metr_preset_repository.get_all()
        self.assertEqual(len(presets), 0)

    def test_get_all_returns_all_saved_presets(self):
        metr_preset_repository.save(self.preset_60)
        metr_preset_repository.save(self.preset_120)

        presets = metr_preset_repository.get_all()
        self.assertEqual(len(presets), 2)
        self.assertEqual(presets[0].bpm, self.preset_60.bpm)
        self.assertEqual(presets[0].beats_per_bar, self.preset_60.beats_per_bar)
        self.assertEqual(presets[1].bpm, self.preset_120.bpm)
        self.assertEqual(presets[1].beats_per_bar, self.preset_120.beats_per_bar)
    
    def test_deleting_preset_removes_preset(self):
        metr_preset_repository.save(self.preset_120)
        metr_preset_repository.save(self.preset_60)
        metr_preset_repository.save(self.preset_180)
        metr_preset_repository.delete(self.preset_60.id)
        presets = metr_preset_repository.get_all()

        self.assertEqual(len(presets), 2)
        self.assertEqual(presets[0].bpm, self.preset_120.bpm)
        self.assertEqual(presets[0].beats_per_bar, self.preset_120.beats_per_bar)
        self.assertEqual(presets[1].bpm, self.preset_180.bpm)
        self.assertEqual(presets[1].beats_per_bar, self.preset_180.beats_per_bar)
  
    def test_updating_preset_changes_values_correctly(self):
        saved_preset = metr_preset_repository.save(self.preset_60)
        new_bpm = 80
        new_beats_per_bar = 4
        new_label = "4-beat"
        saved_preset.bpm = new_bpm
        saved_preset.beats_per_bar = new_beats_per_bar
        saved_preset.label = new_label

        updated_preset = metr_preset_repository.update(saved_preset)
        self.assertEqual(updated_preset.bpm, new_bpm)
        self.assertEqual(updated_preset.beats_per_bar, new_beats_per_bar)
        self.assertEqual(updated_preset.label, new_label)
