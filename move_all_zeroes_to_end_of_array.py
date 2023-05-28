class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_count] = nums[i]
                non_zero_count += 1

        while non_zero_count < len(nums):
            nums[non_zero_count] = 0
            non_zero_count += 1

        return nums


nums = [0,1,0,3,12, 2, 0, 0, 5, 10]
s = Solution()
print(s.moveZeroes(nums))
