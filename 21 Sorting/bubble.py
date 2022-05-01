def Bubble(A):
    n = len(A)
    for i in range(n):
        for j in range(0,n-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A

if __name__ == "__main__":
    print(Bubble([23,3,4,55,6,6,7,123,4,0]))            