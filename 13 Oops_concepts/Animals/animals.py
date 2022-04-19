class Animal:
    def __init__(self,name,legs,has_tail):
        print("Animals constructor is called")
        self.name = name
        self.legs = legs
        self.has_tail = has_tail

    def eat(self):
        print(f"{self.name} is eating")

    def walk(self):
        print(f"{self.name} is walking")