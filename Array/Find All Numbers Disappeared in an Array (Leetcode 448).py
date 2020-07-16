class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        static = 0
        flag =[0] * len(nums)

        for i in nums :
            flag[i-1] = 1
        
        
        for i in range(length) :
            if not flag[i] :
                nums[static] = i + 1
                static += 1

        del nums[static : length]    
        return nums

sol = Solution()
print(sol.findDisappearedNumbers([4,3,2,7,8,2,3,1]))