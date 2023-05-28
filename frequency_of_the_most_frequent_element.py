class Solution:
    def maxFrequency(self, nums, k):
        nums.sort()
        total = 0
        res = 0
        i = 0
        for j in range(len(nums)):
            total += nums[j]
            while nums[j] * (j - i + 1) > total + k:
                total -= nums[i]
                i += 1

            res = max(res, j - i + 1)

        return res


nums = [1, 2, 4]
k = 5
s = Solution()
print(s.maxFrequency(nums, k))

# *********************************************

nums = [1, 2, 4, 4]
k = 5
nums.sort()
res = 0
total = 0
i = 0
for j in range(len(nums)):
    total += nums[j]
    while nums[j] * (j - i + 1) > total + k:
        total -= nums[i]
        i += 1
    res = max(res, j - i + 1)

print(res)
