import unittest

from neural_lab.cache import LRUCache


class CacheTests(unittest.TestCase):
    def test_evicts_least_recently_used(self):
        cache = LRUCache[str, int](2)
        cache.put("a", 1)
        cache.put("b", 2)
        cache.get("a")
        cache.put("c", 3)
        self.assertIsNone(cache.get("b"))
        self.assertEqual(cache.get("a"), 1)


if __name__ == "__main__":
    unittest.main()
