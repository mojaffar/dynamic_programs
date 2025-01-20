class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # removed left while space if it has
        if not s:  # check still do we have string or not, if it is string then process or else will return 0
            return 0

        i = 0
        sign = 1
        # need to check for (+, -) sign
        if s[0] == '+':
            i += 1
        elif s[0] == '-':
            sign = -1
            i += 1

        num = 0
        while i < len(s):
            cur = s[i]
            if not cur.isdigit():  # check if firt item is not digit the break and come out from the loop else make numbers like else part we can see
                break
            else:
                num = num * 10 + int(cur)
            i += 1

        num *= sign

        if num > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif num < -2 ** 31:
            return -2 ** 31
        else:
            return num


st = "  1234q"
sol= Solution()
print(sol.myAtoi(st))





