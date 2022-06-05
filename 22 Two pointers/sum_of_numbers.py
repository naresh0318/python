"""
# basic approch (o(n2))........................................
def solve(sum,a):
    n = len(a)
    for i in range(n):
        for j in range(i+1,n):
            if a[i]+a[j] == sum:
                return True
     
    return False

if __name__ == "__main__":
    sum = int(input())
    a = [1,3,5,2,7,9,78]
    print(solve(sum,a))

"""

"""
#another apporch (0(nlogn)).................
def solve(sum,a):
    a.sort()
    n = len(a)
    left = 0
    right = n-1
    
    while left < right:
        target = a[left] + a[right]
        if target < sum:
            left += 1

        elif target > sum:
            right -= 1

        elif target == sum:
            return True
    
    return False

if __name__ == "__main__":
    a = [21,34,45,56,76,8,45]
    print("Enter the sum")
    sum = int(input())
    print(solve(sum,a))
"""

#another aporch (0(n))...................................
def solve(target,a):
    empty_dict = dict()
    for i in a:
        if target - i in empty_dict:
            return True
        
        empty_dict[i] = True

    return False

if __name__ == "__main__":
    a = [12,234,45,6,78,900]
    target = 18
    print(solve(target,a))