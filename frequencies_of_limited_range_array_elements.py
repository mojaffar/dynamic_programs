arr = [10, 20, 30, 30, 30, 40, 50, 50, 50, 50, 70]
temp_dict = {}
for i in arr:
    if i in temp_dict:
        temp_dict[i] += 1
    else:
        temp_dict[i] = 1

print(temp_dict)

for i, j in temp_dict.items():
    print(i, '--', j)

