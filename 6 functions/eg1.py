"""
# star pattern

def star():
    for i in range(1,n+1):
        for j in range(0,i):
            print('*',end = "")
        print()
print("enter any number = ",end = "")

n = int(input())
star()

"""

# star pattern triangle

def triangle(n):
    k = n - 1
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
            k = k - 1
        for j in range(0, i+1):
            # printing stars
            print("* ", end="")
        print("\r")
n = 4
triangle(n)






