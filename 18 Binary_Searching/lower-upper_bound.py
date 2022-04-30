# example 1
"""
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
"""

#example 2

def lowerbound(A, target) -> int:
    n = len(A)

    left = 0
    right = n-1

    ans = -1

    while left <= right:
        mid = left+right >> 1
        if A[mid] == target:
            ans = mid
            right = mid -1

        elif A[mid] > target:
            right = mid +1

        elif A[mid] < target:
            left = mid +1

    return ans


def upperbound(A, target) -> int:
    n = len(A)

    left = 0
    right = n-1

    ans = -1

    while left <= right:
        mid = left+right >> 1
        if A[mid] == target:
            ans = mid
            left = mid + 1

        elif A[mid] > target:
            right = mid - 1

        elif A[mid] < target:
            left = mid + 1

    return ans


if __name__ == "__main__":
    A = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
    print(lowerbound(A,5),upperbound(A,5))
