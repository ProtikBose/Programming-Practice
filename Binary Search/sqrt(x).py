import math

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 0, x+1
        while left < right:
            mid = left + int(math.floor(float(right - left) / 2.0))
            if mid*mid >x:
                right = mid
            else:
                left = mid + 1
                
        
        return left-1

nums = 9
sol = Solution()
print(sol.mySqrt(nums))