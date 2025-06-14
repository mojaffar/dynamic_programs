from typing import List


def binarySearch(arr, x):

    start = 0
    end = len(arr)-1
    while start<=end:
        mid = (start + end)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < arr[end]:
            start=mid+1

        else:
            end = mid-1

    return -1

arr = [2, 3, 4, 10, 40]
x = 10
# print(binarySearch(arr, x))

def binaryRecursiveSerach(arr, start, end, x):
    while start<=end:
        mid = (start+end)//2
        if arr[mid] == x:
            return mid
        elif arr[mid]<arr[end]:
            return binaryRecursiveSerach(arr, mid+1, end, x)
        else:
            return binaryRecursiveSerach(arr, start, mid-1, x)

    return -1


arr = [2, 3, 4, 10, 40]
x = 10
start = 0
end = len(arr)-1
# print(binaryRecursiveSerach(arr, start, end, x))

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums)-1
        while l<r:
            if nums[l]<=nums[r]:
                res = min(res, nums[l])
                break
            mid = (l+r)//2
            res = min(res, nums[mid])
            if nums[mid]>=nums[l]:
                l+=mid
            else:
                r-=mid

        return res


nums = [3,4,5,1,2]
sol = Solution()
print(sol.findMin(nums))
