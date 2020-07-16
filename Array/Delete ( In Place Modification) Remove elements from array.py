class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
    
        nums = [ele for ele in nums if not ele == val]

        print(nums)       
        #return len(nums)
                

sol = Solution()
sol.removeElement([0,1,2,2,3,0,4,2],2)