import math
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # binary search mainly works for sorted array,
        # but it only works for unsorted array, if the array is rotated
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + int(math.floor(float(right - left) / 2.0))
            if nums[mid] >= nums[right]:
                right = mid
            else:
                left = mid + 1
            print(mid)
        return nums[left]

nums = [4,5,6,7,0,1,2]

sol = Solution()
print(sol.findMin(nums))