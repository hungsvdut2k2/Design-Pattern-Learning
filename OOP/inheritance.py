from abc import abstractclassmethod

class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractclassmethod
    def speak(self):
        pass

class Dog(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name)
    
    def speak(self):
        return f"{self.name} bark"

class Cat(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name)
    
    def speak(self):
        return f"{self.name} meow"
    
if __name__ == "__main__":
    dog = Dog(name="leo bong")
    print(dog.speak())
    cat = Cat(name="mimi")
    print(cat.speak())