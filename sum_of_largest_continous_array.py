arr = [1, -2, 3, 4, -4, 6, -4, 8, 2]
res = 0
total = 0
i = 0

while i < len(arr):
    total = total + arr[i]
    if total < 0:
        total = 0
    if res < total:
        res = total

    i += 1

print(res)
