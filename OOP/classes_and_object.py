class Greeting:
    def __init__(self, name: str):
        self.name = name
    
    def say_hello(self):
        return f"Hello {self.name}"
    
if __name__ == "__main__":
    greeting = Greeting("David")

    print(greeting.say_hello())