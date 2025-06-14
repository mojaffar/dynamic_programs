# 1
arr =[1, 2, 3, 1, 4, 5, 2, 3, 6]
k = 3

#output = [3, 3, 4, 5, 5, 5, 6]

if k>len(arr):
    print("invalid")

res = []
for i in range(len(arr)-k+1):
    windows = arr[i:i+k]
    res.append(max(windows))

# print(res)


