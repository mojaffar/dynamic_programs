from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = -1  # Initialize pivot

        # Step 1: Find pivot (first element from right that is smaller than its next)
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                pivot = i - 1
                break

                # If no pivot is found, reverse the entire array (last permutation case)
        if pivot == -1:
            nums.reverse()
            return

        # Step 2: Find the smallest element greater than pivot, from the right side
        swap = len(nums) - 1
        while nums[swap] <= nums[pivot]:
            swap -= 1

        # Step 3: Swap pivot and swap elements
        nums[pivot], nums[swap] = nums[swap], nums[pivot]

        # Step 4: Reverse elements after pivot (to get next lexicographical order)
        nums[pivot + 1:] = reversed(nums[pivot + 1:])

        return nums



num = [1,2,3]
sol = Solution()
print(sol.nextPermutation(num))