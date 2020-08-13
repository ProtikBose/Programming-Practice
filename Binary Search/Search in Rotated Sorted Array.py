import math
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # binary search mainly works for sorted array,
        # but it only works for unsorted array, if the array is rotated
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + int(math.floor(float(right - left) / 2.0))
            if nums[mid] == target :
                return mid
            # the bottom half is sorted
            if nums[left] <= nums[mid] :
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        
            # the upper half is sorted
            else :
                if nums[mid] < target and target <= nums[right] :
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1

nums = [4,5,6,7,0,1,2]
target = 0
sol = Solution()
print(sol.search(nums,target))