def star():    
    print("Enter the number of raw's for star pattern = ",end="")
    n = int(input())
    for i in range(1,n+1):
        spaces = n-i
        print(spaces * " ",end = "")
        print(i * "*")
star()