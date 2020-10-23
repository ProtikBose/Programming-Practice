import math
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def condition(val):
            return nums[val] > nums[val+1]
            
            
            
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + int(math.floor(float(right - left) / 2.0))
            
            if condition(mid):
                right = mid
            else:
                left = mid + 1
            
        return left