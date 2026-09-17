import unittest

from neural_lab.evaluation import hit_rate, precision_at_k, reciprocal_rank


class EvaluationTests(unittest.TestCase):
    def test_reciprocal_rank(self):
        self.assertEqual(reciprocal_rank(["a", "b", "c"], {"b"}), 0.5)

    def test_precision_at_k(self):
        self.assertEqual(precision_at_k(["a", "b", "c"], {"a", "c"}, 2), 0.5)

    def test_hit_rate(self):
        self.assertEqual(hit_rate(["a", "b"], {"b"}, 2), 1.0)
        self.assertEqual(hit_rate(["a", "b"], {"z"}, 2), 0.0)


if __name__ == "__main__":
    unittest.main()
