from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            n = nums[i]
            temp = nums[:i] + nums[i+1:]

            perms = self.permute(temp)

            for perm in perms:
                perm.append(n)

            res.extend(perms)

        return res


nums = [1,2,3]
sol = Solution()
print(sol.permute(nums))


