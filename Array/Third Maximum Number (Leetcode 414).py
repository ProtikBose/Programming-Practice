class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxList = [float('-inf')] * 3

        for i in range(len(nums)) :
            
            if nums[i] not in maxList :
                if nums[i] > maxList[0] :
                    maxList = [ nums[i] , maxList[0] , maxList[1]]
                elif nums[i] > maxList[1] :
                    maxList = [ maxList[0] , nums[i] , maxList[1]]
                elif nums[i] > maxList[2] :
                    maxList = [ maxList[0] , maxList[1] , nums[i]]

        return max(maxList) if float('-inf') in maxList else maxList[2]

sol = Solution()
print(sol.thirdMax([2,2,3,1]))