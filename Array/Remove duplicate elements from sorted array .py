class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not len(nums) :
            return 0

        current = 1
        static = 0

        while current < len(nums) :

            if not nums[current] == nums[static] :
                
                static += 1
                nums[static] = nums[current]
            
            current += 1

        return static + 1

