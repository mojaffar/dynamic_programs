# First way
nums = [2, 7, 11, 15]
target = 9

res = []

for i in range(len(nums)):
    for j in range(i, len(nums)):
        if nums[i] + nums[j] == target:
            res.append(i)
            res.append(j)

print(res)

# Anotherway using dic

nums = [2, 7, 11, 15]
target = 9
temp = {}
res = []
for i, j in enumerate(nums):
    dif = target - nums[i]
    if dif in temp:
        print(temp[dif], i)
    temp[j] = i



