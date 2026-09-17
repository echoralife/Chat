import unittest

from neural_lab.decay import exponential_decay


class DecayTests(unittest.TestCase):
    def test_half_life(self):
        self.assertAlmostEqual(exponential_decay(72, 72), 0.5)

    def test_fresh_memory(self):
        self.assertAlmostEqual(exponential_decay(0), 1.0)


if __name__ == "__main__":
    unittest.main()
