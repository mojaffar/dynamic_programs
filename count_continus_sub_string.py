str1 = "abcabdabcacdabc"
str2 = 'abc'

n = len(str1)
m = len(str2)

count = 0

for i in range(n-m+1):
    if str1[i:i+m] == str2:
        count +=1

print(count)