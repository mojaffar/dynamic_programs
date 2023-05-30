# https://leetcode.com/problems/find-all-duplicates-in-an-array/submissions/959975720/
nums = [4, 3, 2, 7, 8, 2, 3, 1]

res = []
test_dict = {}

for i in nums:
    if i in test_dict:
        test_dict[i] += 1
    else:
        test_dict[i] = 1

for key, value in test_dict.items():
    if value > 1:
        res.append(key)

print(res)

# *****************************

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        hm = {}
        for i in nums:
            if i in hm:
                hm[i] += 1
            else:
                hm[i] = 1

        for i, j in hm.items():
            if j > 1:
                res.append(i)

        return res