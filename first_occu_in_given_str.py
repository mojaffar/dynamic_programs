class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        l1 = len(haystack)
        l2 = len(needle)

        if l2 == 0:
            return 0

        for i in range(l1 - l2 + 1):
            if haystack[i:i+l2] == needle:
                return i

        return -1


haystack = "sadbutsad"
needle = "sad"
sol = Solution()
print(sol.strStr(haystack, needle))
