def printstar(n):
    
    for raw in range(1,n+1):
        for star in range(raw):
            print("*",end="")
        print()

printstar(7)