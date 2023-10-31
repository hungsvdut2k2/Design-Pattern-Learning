import unittest
from unittest import TestCase
from vehicles import (
    Car,
    Bicycle,
    Boat,
)  # Assuming you have saved the Vehicle classes in a file named 'vehicles.py'


class Evaluate(TestCase):
    def test_car_move(self):
        car = Car()
        self.assertEqual(car.move(), "The car is driving.")

    def test_bicycle_move(self):
        bicycle = Bicycle()
        self.assertEqual(bicycle.move(), "The bicycle is pedaling.")

    def test_boat_move(self):
        boat = Boat()
        self.assertEqual(boat.move(), "The boat is sailing.")


if __name__ == "__main__":
    unittest.main()
