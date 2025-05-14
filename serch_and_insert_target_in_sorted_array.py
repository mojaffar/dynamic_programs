# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         l, r = 0, len(nums) - 1
#         while l <= r:
#             middle = (l + r) // 2
#
#             if nums[middle] == target:
#                 return middle
#
#             if target > nums[middle]:
#                 l = middle + 1
#             if target < nums[middle]:
#                 r = middle - 1
#
#         return l
from functools import reduce

l = [3,1,4, 22, 45, 1, 245, 6, 34, 4, 8, 14]
sum = reduce((lambda a, b:a+b*2), l, 1000)
print(sum)