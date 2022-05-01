def selection(A):
    n = len(A)
    for i in range(n):
        min_ele = A[i]
        min_else_idx = i
        for idx in range(i, len(A)):
            if A[idx] < min_ele:
                min_ele = A[idx]
                min_else_idx = idx
            
        A[i], A[min_else_idx] = A[min_else_idx], A[i]

    return A

if __name__ == "__main__":
    print(selection([23,43,5,67,8,9,0,1,111]))