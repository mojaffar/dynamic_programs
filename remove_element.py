from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        left = 0

        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left+=1

            elif nums[right] == val:
                continue

        return left


nums = [3,2,2,4,3]
val=3
sol = Solution()
print(sol.removeElement(nums, val))