def lower_bound(A, target):
    prev = -1
    for i in range (len(A)):
        if A[i] == target:
            return i
        
        elif A[i] > target:
            return prev
        
        prev = i

if __name__ == "__main__":
    print(lower_bound([12,23,23,34,45,56,78,99],90))