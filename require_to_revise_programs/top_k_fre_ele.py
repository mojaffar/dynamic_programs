from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # to data in key val pair in hashmap
        hashmap = {}
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)

        print(hashmap)

        arr = []
        for key, val  in hashmap.items():
            arr.append([val, key])

        print(arr)
        # sort arr to get item in creasing order
        arr.sort()
        res = []
        for i in range(k):
            res.append(arr.pop()[1])

        return res


nums = [1,1,1,2,2,3]
k = 2
s = Solution()
print(s.topKFrequent(nums, k))


