nums = [0, 1, 1, 0, 0, 2, 1, 2, 2]
low = 0
high = len(nums) - 1
mid = 0

while mid <= high:
    if nums[mid] == 0:
        nums[low], nums[mid] = nums[mid], nums[low]
        low += 1
        mid += 1
    elif nums[mid] == 1:
        mid += 1
    else:
        nums[mid], nums[high] = nums[high], nums[mid]
        high -= 1

print(nums)
