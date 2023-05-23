def rec(arr, idx):
    if idx >= len(arr):
        return 0
    return max(arr[idx] + rec(arr, idx + 2), rec(arr, idx + 1))


def findMaxSum(arr, n):
    return rec(arr, 0)


arr = [5, 5, 10, 100, 10, 5]
N = len(arr)
print(findMaxSum(arr, N))
