from math import factorial
from tkinter import N


def Factorial(n):
    if n == 1:
        return 1

    fact = n * Factorial(n-1)
    return fact

if __name__ == "__main__":
    n =5
    print(n,"'s Facorial is =",Factorial(n))