from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0
        for n in nums:
            if (n-1) in hashset:
                length = 0
                while (n+length) in hashset:
                    length +=1
                longest = max(length, longest)
        return longest


nums = [100,4,200,1,3,2]
s = Solution()
print(s.longestConsecutive(nums))