arr = [15, -2, 2, -8, 1, 7, 10, 13]

# Using bruce force concept t.c = o(n*n), sc = 1
max_len = 0

for i in range(len(arr)):
    current_sum = 0
    for j in range(i, len(arr)):
        current_sum += arr[j]
        if current_sum == 0:
            max_len = max(max_len, j-i+1)
print(max_len)

# Using has map concept t.c = o(n), sc = o(n)

arr = [15, -2, 2, -8, 1, 7, 10, 13]

test_dict = {}
max_len = 0
current_sum = 0

for i in range(len(arr)):
    current_sum += arr[i]
    if current_sum == 0:
        max_len = i+1

    if current_sum in test_dict:
        max_len = max(max_len, i - test_dict[current_sum])
    else:
        test_dict[current_sum] = i

print(max_len)










