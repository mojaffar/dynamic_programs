from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])

        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1

            while l<r:
                three_sum = nums[i] + nums[l] + nums[r]
                if abs(three_sum-target) < abs(res-target):
                    res = three_sum
                elif three_sum < target:
                    l+=1
                else:
                    r-=1

        return res


nums = [-1,2,1,-4]
target = 1
sol = Solution()
print(sol.threeSumClosest(nums, target))