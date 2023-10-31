import unittest
from unittest import TestCase
from devices import (
    Smartphone,
    Laptop,
    Smartwatch,
)  # Assuming you have saved the ElectronicDevice classes in a file named 'devices.py'


class Evaluate(TestCase):
    def test_smartphone_battery_life(self):
        smartphone = Smartphone()
        self.assertEqual(
            smartphone.battery_life(), "Smartphone battery life: 10 hours."
        )

    def test_laptop_battery_life(self):
        laptop = Laptop()
        self.assertEqual(laptop.battery_life(), "Laptop battery life: 5 hours.")

    def test_smartwatch_battery_life(self):
        smartwatch = Smartwatch()
        self.assertEqual(
            smartwatch.battery_life(), "Smartwatch battery life: 24 hours."
        )


if __name__ == "__main__":
    unittest.main()
