import unittest

from neural_lab.chunking import chunk_words


class ChunkingTests(unittest.TestCase):
    def test_overlap_is_preserved(self):
        chunks = chunk_words("one two three four five six", size=4, overlap=2)
        self.assertEqual(chunks[0], "one two three four")
        self.assertEqual(chunks[1], "three four five six")

    def test_invalid_overlap_raises(self):
        with self.assertRaises(ValueError):
            chunk_words("hello", size=4, overlap=4)


if __name__ == "__main__":
    unittest.main()
