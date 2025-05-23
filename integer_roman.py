class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = [
            ["I", 1],
            ["IV", 4],
            ["V", 5],
            ["IX", 9],
            ["X", 10],
            ["XL", 40],
            ["L", 50],
            ["XC", 90],
            ["C", 100],
            ["CD", 400],
            ["D", 500],
            ["CM", 900],
            ["M", 1000]
        ]
        res = ""
        for sym, val in reversed(symbols):
            if num//val:
                count = num // val
                res += (sym * count)
                num = num % val
        return res


num = 3749
sol = Solution()
print(sol.intToRoman(num))