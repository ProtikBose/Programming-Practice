import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        epsilon = .0000000001
        if n<=0 :
            return False
        return (math.log(n) / math.log(3) + epsilon) % 1 <= 2 * epsilon

        
n = 728
sol = Solution()
print(sol.isPowerOfThree(n))
