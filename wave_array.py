def wave(arr):
    arr.sort()
    for i in range(1, len(arr), 2):
        arr[i], arr[i-1] = arr[i-1], arr[i]

    return arr


arr = [10, 90, 49, 2, 1, 5, 23]
res = wave(arr)
print(res)


###########
arr = [10, 90, 49, 2, 1, 5, 23]
arr.sort()
for i in range(1, len(arr), 2):
    arr[i], arr[i-1] = arr[i-1], arr[i]

print(arr)
