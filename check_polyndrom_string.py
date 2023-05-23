s = 'madam'
start = 0
end = len(s) - 1
mid = (start + end) // 2
flag = 0

while start < mid:
    if s[start] == s[end]:
        start += 1
        end -= 1
        flag = 1
    else:
        flag = 0
        break

if flag == 1:
    print('yes')
else:
    print('no')
