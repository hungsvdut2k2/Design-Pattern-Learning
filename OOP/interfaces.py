from abc import ABC, abstractclassmethod

class MyInterface(ABC):
    @abstractclassmethod
    def my_method(self):
        pass

class MyClass(MyInterface):
    def my_method(self):
        return "leo bong"


if __name__ == "__main__":
    my_obj = MyClass()
    print(my_obj.my_method())