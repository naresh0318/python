def Binary_searching(A,tareget):
    left = 0
    right = len(A) -1

    while left <= right:
        mid = (left+right) // 2

        if A[mid] == tareget:
            return mid
        elif A[mid] > tareget:
            right = mid - 1

        else:
            left = mid + 1

    return None
if __name__ == "__main__":
    print(Binary_searching([23,34,45,56,67,78,89,90,990],23))


