"""

class Bank:
    def __init__(self, name):
        self.name = name
        self.amount = 0
    
    def add_amount(self,a):
        self.amount += a

class HDFC(Bank):
    def __init__(self):
        name = "HDFC"
        super().__init__(name)
        
if __name__ == "__main__":
    B = HDFC()
    B.add_amount(100)
    print(B.amount)

....................................................................
"""

"""
Polymorphism
"""
"""

from unicodedata import name


class Shape:
    def __init__(self,name):
        self.name = name

class Square(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    def area(self):
        return self.side * self.side

class Rectangle(Shape):
    def __init__(self, name, x, y):
        super().__init__(name)
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

if __name__ == "__main__":
    s = Square("s",3)
    print(s.name,". Square area is : ",s.area())

    r = Rectangle("r",15,3)
    print(r.name,". Rectangle area is : ",r.area())


....................................................................
"""

"""
Payment
"""
class Payment:
    def __init__(self, amount):
        self.amount = amount

    def make_payment(self):
        print("initiating payment")
        self.pay()

    def pay(self):
        print("Default payment")


class COD(Payment):
    def __init__(self, amount):
        super().__init__(amount)

    def pay(self):
        print("Paying from cod")

    
class CREDIT_CARD(Payment):
    def __init__(self, amount):
        super().__init__(amount)

    def pay(self):
        print("Paying from CREDIT CARD",self.amount)


if __name__ == "__main__":
    cod = COD(23000)
    cod.make_payment()

    cc = CREDIT_CARD(220000)
    cc.make_payment()