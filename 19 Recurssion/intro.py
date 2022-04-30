cnt = 0
def Hello():
    global cnt
    if cnt == 1: # this is called Base condition
        return 

    print("Hi")
    cnt += 1
    Hello()

if __name__ == "__main__":
    Hello()