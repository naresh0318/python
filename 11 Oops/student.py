# creating our first class...
import random
class Student_info:
    def __init__(self,name,age,Birth_Year): 
        self.name = name
        self.age = age
        self.Birth_Year = Birth_Year
    
    def read(self):
        print("Student "f"{self.name} is reading")
    
    def write(self):
        print("Student "f"{self.name} is writing")

    def give_mcq(self):
        sub = ["Maths","Computer","Physics"]
        random_subject = sub[random.randint(0,len(sub)-1)]
        print(f"{self.name} gave mcq on class {random_subject}")
        print(f"{self.name} get marks {random.randint(34,100)} in {random_subject}")