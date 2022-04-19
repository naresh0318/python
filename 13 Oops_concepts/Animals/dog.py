from Animals.animals import Animal



class Dog(Animal):
        def __init__(self,name,legs,has_tail):
            super().__init__(name,legs,has_tail)
            print("Dog is an animal")
        
        def bark(self):
            print(f"{self.name} is barking")
