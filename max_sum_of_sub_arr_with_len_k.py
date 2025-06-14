# arr = [100, 200, 300, 400]
# k = 2
#
# res = 0
# for i in range(len(arr)-k+1):
#     current_sum = 0
#     for j in range(k):
#         current_sum = current_sum + arr[i +j]
#
#     res = max(current_sum, res)
#
# print(res)

def maxSum(arr, n, k):
    if n < k:
        return "invalid"

    res = sum(arr[:k])
    maxS = res

    for i in range(k, n):
        res = res - arr[i - k] + arr[i]
        maxS = max(res, maxS)

    return maxS

# Driver code
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
n = len(arr)
print(maxSum(arr, n, k))  # Output: 24

