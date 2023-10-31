import math
import unittest
from circle import Circle  # Assuming you have saved the Circle class in a file named 'circle.py'


class Evaluate(unittest.TestCase):
    def test_area(self):
        circle1 = Circle(3)
        circle2 = Circle(5)

        self.assertAlmostEqual(circle1.area(), math.pi * 3 ** 2, places=5)
        self.assertAlmostEqual(circle2.area(), math.pi * 5 ** 2, places=5)

    def test_circumference(self):
        circle1 = Circle(3)
        circle2 = Circle(5)

        self.assertAlmostEqual(circle1.circumference(), 2 * math.pi * 3, places=5)
        self.assertAlmostEqual(circle2.circumference(), 2 * math.pi * 5, places=5)

    def test_diameter(self):
        circle1 = Circle(3)
        circle2 = Circle(5)

        self.assertEqual(circle1.diameter(), 2 * 3)
        self.assertEqual(circle2.diameter(), 2 * 5)


if __name__ == '__main__':
    unittest.main()