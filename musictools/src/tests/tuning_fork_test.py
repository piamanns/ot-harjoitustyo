import unittest
from entities.tuning_fork import TuningFork


class TestTuningFork(unittest.TestCase):
    def setUp(self):
        self.tuning_fork = TuningFork()

    def test_setting_tuning_fork_frequency_updates_frequency_correctly(self):
        self.tuning_fork.set_frequency(650)
        self.assertEqual(self.tuning_fork.get_frequency(), 650)
    
    def test_setting_tuning_fork_to_non_float_freq_does_nothing(self):
        self.tuning_fork.set_frequency(440)
        self.tuning_fork.set_frequency("abc")
        self.assertEqual(self.tuning_fork.get_frequency(), 440)

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
