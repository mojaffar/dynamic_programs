# s = 'madam'
# start = 0
# end = len(s) - 1
# mid = (start + end) // 2
# flag = 0
#
# while start < mid:
#     if s[start] == s[end]:
#         start += 1
#         end -= 1
#         flag = 1
#     else:
#         flag = 0
#         break

# if flag == 1:
#     print('yes')
# else:
#     print('no')



class Solution:
    def isPalindrome(self, s: str) -> bool:
        # using two pointers
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

        # # using binary search
        # temp = [ch.lower() for ch in s if ch.isalnum()]
        # print(temp)
        # start = 0
        # end = len(temp)-1
        # mid = (start + end)//2
        # while start<mid:
        #     if temp[start] != temp[end]:
        #         return False
        #     start+=1
        #     end -=1
        #
        # return True


sample = "A man, a plan, a canal: Panama"
# sample = "race a car"
s = Solution()
print(s.isPalindrome(sample))