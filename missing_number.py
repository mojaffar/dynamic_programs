# first way
nums = [3, 0, 1]
res = []
for i in range(max(nums)+1):
    if i not in nums:
        res.append(i)

print(res)

# second way
nums = [3, 0, 1]
n = len(nums)
actual_total = int(n * (n + 1) / 2)
total = sum(nums)
print(actual_total-total)

# third way
nums = [0, 1, 3, 5, 6, 7, 10]
start = nums[0]
end = max(nums)+1
missing_number = []

for i in range(start, end):
    if i not in nums:
        missing_number.append(i)

print(missing_number)



