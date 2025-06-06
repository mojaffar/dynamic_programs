from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i]*=postfix
            postfix *= nums[i]

        return  res
        # using using bruit force
        # res = []
        # for i in range(len(nums)):
        #     prod = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         prod *=nums[j]
        #     res.append(prod)
        #
        # return res




nums = [1,2,3,4]
s = Solution()
print(s.productExceptSelf(nums))
