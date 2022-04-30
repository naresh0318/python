class Solution:
    def findpeekelement(self, nums):
        n = len(nums)
        for i in range(n):
            if i == 0:
                if nums[i] > nums[i+1]:
                    return i,nums[i]
            
            elif i == n - 1:
                if nums[i] > nums[i-1]:
                    return i,nums[i]
            
            else:
                if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                    return i,nums[i]
                     


sol = Solution()
print(sol.findpeekelement([1,1,1,12,3]))    

def solve(A):
    left = 0
    right = len(A) - 1
    while left <= right:
        mid = left + right >>1
        if mid == 0 and A[mid + 1] <A[mid]:
            return mid

        if mid == len(A) - 1 and A[mid] > A[mid -1]:
            return mid
        
        if A[mid] >= A[mid -1] and A[mid] > A[mid+1]:
            return mid

        elif A[mid + 1] > A[mid]:
            left = mid + 1

        elif A[mid - 1] > A[mid]:
            right = mid - 1
    
if __name__ == "__main__":
    A = [1,2,34,454,56,7]
    print(solve(A))