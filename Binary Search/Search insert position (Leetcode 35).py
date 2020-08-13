import math
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)
        while left < right:
            mid = left + int(math.floor(float(right - left) / 2.0))
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        # After commenting this out, we can tell the position of a number which does not exist
        # in the given array        
        '''        
        if left == len(nums) or nums[left] != target :
            return -1
        '''
        return left