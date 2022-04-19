"""
for i in range(101):
    if i%2 == 0:
        print("num is even = ",i)
    else:
        print("num is odd  = ",i)
"""
print("enter any number")
user = int (input())
print("the number is = ",user)
for i in range(1, user + 1):
    if i%3 == 0:
        print("FIZZ")
    elif i%5 == 0:
        print("FUZZ")
    else :
        print(i)
