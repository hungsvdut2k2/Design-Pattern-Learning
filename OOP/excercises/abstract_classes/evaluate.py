import unittest
from unittest import TestCase
from shapes import Shape, Rectangle, Circle


class Evaluate(TestCase):
    def setUp(self):
        self.rectangle1 = Rectangle("red", 4, 5)
        self.circle1 = Circle("blue", 3)

    def test_rectangle_area(self):
        self.assertAlmostEqual(self.rectangle1.area(), 20)

    def test_rectangle_perimeter(self):
        self.assertAlmostEqual(self.rectangle1.perimeter(), 18)

    def test_circle_area(self):
        self.assertAlmostEqual(self.circle1.area(), 28.274333882308138)

    def test_circle_perimeter(self):
        self.assertAlmostEqual(self.circle1.perimeter(), 18.84955592153876)


if __name__ == "__main__":
    unittest.main()
