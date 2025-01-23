from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l<r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum>0:
                    r-=1
                elif three_sum<0:
                    l+=1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # remove duplicates elements from the results eg = [-1,-1,0,0,1,1]
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return res

        # for i, v in enumerate(nums):
        #     if i > 0 and v == nums[i-1]:
        #         continue
        #     l, r = i+1, len(nums)-1
        #
        #     while l<r:
        #         three_sum = v + nums[l] + nums[r]
        #         if three_sum>0:
        #             r-=1
        #         elif three_sum<0:
        #             l+=1
        #         else:
        #             res.append([v, nums[l], nums[r]])
        #             # if case of [-2,-2,0,0,2,2] need to remove duplicates or change the l, r position
        #             l+=1
        #             while nums[l]== nums[l-1] and l<r:
        #                 l+=1
        # return res

nums = [-1,0,1,2,-1,-4]
sol = Solution()
print(sol.threeSum(nums))

