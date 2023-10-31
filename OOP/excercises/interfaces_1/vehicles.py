from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        return "The car is driving."


class Bicycle(Vehicle):
    def move(self):
        return "The bicycle is pedaling."


class Boat(Vehicle):
    def move(self):
        return "The boat is sailing."
