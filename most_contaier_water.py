from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0 # Brute force
        for l in range(len(height)):
            for r in range(l+1, len(height)):
                area= (r-l) * min(height[l], height[r])
                res = max((res, area))
        return res



height = [1,8,6,2,5,4,8,3,7]
sol = Solution()
print(sol.maxArea(height))

# But above solution did not work in terms of time complexity, it takes a tol execution time so will
# reject but to understander area it will br good reference
# so will do using two point concept

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0 # two pointers concepts
        l, r = 0, len(height)-1
        while l<r :
            area = (r-l)*min(height[l], height[r])
            res = max(res, area)

            if height[l]<height[r]:
                l+=1
            elif height[l]>height[r]:
                r -=1
            else:
                l+=1

        return res

height = [1,8,6,2,5,4,8,3,7, 8]
sol = Solution()
print(sol.maxArea(height))
