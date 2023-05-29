arr = [15, 2, 4, 8, 9, 5, 10, 23]
target = 23
ans = 0
preSum = 0
d = {0: 1}

for i in arr:
    preSum += i

    if preSum - target in d:
        ans += d[preSum - target]

    if preSum not in d:
        d[preSum] = 1
    else:
        d[preSum] += 1

print(ans)
