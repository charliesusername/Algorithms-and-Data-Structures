import unittest
from maximum_loot import maximum_loot_value


class TestMaximumLoot(unittest.TestCase):
    def test(self):
        for (capacity, weights, prices, answer) in [
            (50, [20, 50, 30], [60, 100, 120], 180.0),
            (10, [30], [500], 500/3),
            (30, [10, 30, 20], [10, 15, 40], 50),
            (100, [20, 40, 10], [50, 5, 10], 65),
            (5, [1, 2, 2, 3], [6, 4, 4, 3], 14),
            (0, [30], [500], 0)
        ]:
            self.assertAlmostEqual(
                maximum_loot_value(capacity, weights, prices),
                answer,
                delta=1e-03
            )


if __name__ == '__main__':
    unittest.main()



