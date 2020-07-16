class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        static = 0
        numberOfZero = 0

        for i in range(length):
            
            if not nums[i]:
                numberOfZero += 1
            else :
                nums[static] = nums[i]
                static += 1
        
        for i in range(static,length) :
            nums[i] = 0

        return nums

sol = Solution()
print(sol.moveZeroes([0,1,0,3,12]))