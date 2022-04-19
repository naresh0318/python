# sum of cube of numbers 1 to N.

def cube_till_N():
    n = int(input())
    sum = 0
    for i in range(1,n+1):
        sum += i ** 3
    print(sum)
cube_till_N() 