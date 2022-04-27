"""
Decimal to binary
"""
def DtoB(n):
    Binary_string = ""
    while n>0:
        rem = n % 2
        Binary_string += str(rem)
        n //= 2
    
    return Binary_string[::-1]

if __name__ == "__main__":
    print(DtoB(23))