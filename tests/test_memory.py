import unittest

from neural_lab.memory import VectorMemory, cosine_similarity


class VectorMemoryTests(unittest.TestCase):
    def test_identical_vectors_have_unit_similarity(self):
        self.assertAlmostEqual(cosine_similarity([1, 2], [1, 2]), 1.0)

    def test_search_returns_best_match_first(self):
        memory = VectorMemory(2)
        memory.add("x", [1, 0])
        memory.add("y", [0, 1])
        self.assertEqual(memory.search([0.9, 0.1], limit=1)[0].text, "x")

    def test_dimension_mismatch_raises(self):
        memory = VectorMemory(3)
        with self.assertRaises(ValueError):
            memory.add("bad", [1, 2])


if __name__ == "__main__":
    unittest.main()
