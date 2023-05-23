string = "()"
check_brackets = ['[]', '{}', '()']

while any(i in string for i in check_brackets):
    for i in check_brackets:
        string = string.replace(i, '')

if len(string) == 0:
    print('yes')
else:
    print('no')

