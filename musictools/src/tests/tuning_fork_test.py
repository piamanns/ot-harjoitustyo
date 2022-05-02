import unittest
from entities.tuning_fork import TuningFork
from config import TF_BASE_A, TF_FREQ_MIN, TF_FREQ_MAX


class TestTuningFork(unittest.TestCase):
    def setUp(self):
        self.tuning_fork = TuningFork()
    
    def _calculate_frequency(self, half_steps: int, base_a=int(TF_BASE_A)):
        freq = (2 ** (1/12 * half_steps)) * base_a
        return freq 

    def test_setting_tuning_fork_frequency_updates_frequency_correctly(self):
        self.tuning_fork.set_frequency(650)
        self.assertEqual(self.tuning_fork.get_frequency(), 650)
    
    def test_setting_tuning_fork_to_non_float_freq_does_nothing_returns_None(self):
        self.tuning_fork.set_frequency(440)
        freq = self.tuning_fork.set_frequency("abc")
        self.assertEqual(self.tuning_fork.get_frequency(), 440)
        self.assertEqual(freq, None)
    
    def test_setting_tuning_fork_freq_to_less_than_min_value_does_nothing_returns_None(self):
        self.tuning_fork.set_frequency(440)
        freq = self.tuning_fork.set_frequency(-1*int(TF_FREQ_MIN))
        self.assertEqual(self.tuning_fork.get_frequency(), 440)
        self.assertEqual(freq, None)

    def test_setting_tuning_fork_freq_to_more_than_max_value_does_nothing_returns_None(self):
        self.tuning_fork.set_frequency(440)
        freq = self.tuning_fork.set_frequency(int(TF_FREQ_MAX)+1)
        self.assertEqual(self.tuning_fork.get_frequency(), 440)
        self.assertEqual(freq, None)

    def test_tuning_fork_is_active_returns_correct_value_when_tf_not_started(self):
        is_active = self.tuning_fork.is_active()
        self.assertEqual(is_active, False)
    
    def test_tuning_fork_is_active_returns_correct_value_when_tf_was_started(self):
        self.tuning_fork.start()
        is_active = self.tuning_fork.is_active()
        self.assertEqual(is_active, True)
        self.tuning_fork.stop()
    
    def test_tuning_fork_is_active_returns_correct_value_when_tf_was_stopped(self):
        self.tuning_fork.start()
        self.tuning_fork.stop()
        is_active = self.tuning_fork.is_active()
        self.assertEqual(is_active, False)
    
    def test_tuning_fork_returns_correct_note_name_when_freq_higher_than_base_a(self):
        freq = self._calculate_frequency(15)
        name = self.tuning_fork.get_note_name(freq)
        self.assertEqual(name, "C6")

    def test_tuning_fork_returns_correct_note_name_when_freq_lower_than_base_a(self):
        freq = self._calculate_frequency(-14)
        name = self.tuning_fork.get_note_name(freq)
        self.assertEqual(name, "G3")
    
    def test_tuning_fork_returns_correct_note_name_when_freq_in_same_octave_as_base_a(self):
        freq = self._calculate_frequency(-5)
        name = self.tuning_fork.get_note_name(freq)
        self.assertEqual(name, "E4")
    
    def test_tuning_fork_returns_correct_note_name_when_base_a_is_changed(self):
        self.tuning_fork = TuningFork(415, 415)
        name = self.tuning_fork.get_note_name(248.23)
        self.assertEqual(name, "C4")