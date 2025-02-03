from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        for right in range(1, len(nums)):
            if nums[right] != nums[right-1]:
                nums[left] = nums[right]
                left+=1

        return left


nums = [0,0, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5,5, 5,5]
sol = Solution()
print(sol.removeDuplicates(nums))