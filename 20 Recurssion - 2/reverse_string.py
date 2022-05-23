"""
def Reverse(str):
    if str == "":   
        return ""

    rev = str[-1] + Reverse(str[:-1])
    return rev

if __name__ == "__main__":
    str = "ABCDEFGHIJKLMNOPQRSTUWXYZ"
    print("reversal is =",Reverse(str))

"""        

from itertools import count

def R(l):
    if len(l) == 0:
        return 0

    count = 1 + R(l[:-1])
    return count

if __name__ == "__main__":
    print(R([1,2,3,4,5,63,4,11,2,]))