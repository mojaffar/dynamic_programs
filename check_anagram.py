def check_anagram(str1, str2):
    if len(str1) != len(str2):
        return 0

    str1 = sorted(str1)
    str2 = sorted(str2)
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return 0
    return 1


str1 = "test"
str2 = "tset"
res = check_anagram(str1, str2)
if res == 1:
    print('yes')
else:
    print('no')