#!/usr/bin/env python3


import unittest
import doctest

import pyfuck
from pyfuck.png import PNG


class TestPNG(unittest.TestCase):

    def test_doctests(self):
        """
        Runs doctests.
        """
        import random
        result = doctest.testmod(pyfuck.png, extraglobs={"random": random})
        self.assertEqual(result.failed, 0)

    def test_filters(self):
        """
        Tests PNG line filtering.
        """
        p = PNG()
        self.assertEqual(p.load("test/assets/filterSub.png").pixels[-2][-1], (8, 70, 255))
        self.assertEqual(p.load("test/assets/filterUp.png").pixels[-2][-1], (8, 70, 255))
        self.assertEqual(p.load("test/assets/filterAverage.png").pixels[-2][-1], (8, 70, 255))
        self.assertEqual(p.load("test/assets/filterPaeth.png").pixels[-2][-1], (8, 70, 255))

    def test_palette(self):
        """
        Tests PNG palette.
        """
        self.assertEqual(PNG().load("test/assets/palette.png").pixels[-1][-1], (0, 0, 255))


if __name__ == "__main__":
    unittest.main()
