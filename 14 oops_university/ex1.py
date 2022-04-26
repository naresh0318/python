class Animal:
    def __init__(self):
        print("__init__ constructor called")
    
    def walk(self):
        print("animal is walking")

class Dog(Animal):
    def __init__(self):
        super().__init__()
    
    def bark(self):
        print("Dog is barking")

    def walk(self):
        super().walk()

if __name__ == "__main__":
    german_shepherd = Dog()
    german_shepherd.walk()
    german_shepherd.bark()
    german_shepherd.walk()   