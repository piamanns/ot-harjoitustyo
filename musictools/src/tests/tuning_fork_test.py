import unittest
from tuning_fork import TuningFork


class TestTuningFork(unittest.TestCase):
    def setUp(self):
        self.tuning_fork = TuningFork()

    def test_setting_tuning_fork_frequency_updates_frequency_correctly(self):
        self.tuning_fork.set_frequency(650)
        self.assertEqual(self.tuning_fork.get_frequency(), 650)
