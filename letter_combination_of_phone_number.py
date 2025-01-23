from string import digits
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def backtrack(idx, curChar):
            if idx == len(digits):
                res.append(curChar)
                return

            for c in digit_to_letters[digits[idx]]:
                backtrack(idx+1, curChar+c)

        res = []
        backtrack(0, "")

        return res


num = "29"
sol = Solution()
print(sol.letterCombinations(num))