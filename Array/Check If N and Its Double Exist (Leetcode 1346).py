class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        numberMap = {}
        for i in arr :
            if i/2 in numberMap.keys() or 2 * i in numberMap.keys() :
                return True
            numberMap[i] = True

        return False

sol = Solution()
print(sol.checkIfExist([10,2,5,3]))
print(sol.checkIfExist([7,1,14,11]))
print(sol.checkIfExist([3,1,7,11]))

