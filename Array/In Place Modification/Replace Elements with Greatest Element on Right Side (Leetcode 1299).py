class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        currMax = arr[len(arr) - 1]
        arr[len(arr) - 1] = -1

        for i in range(len(arr) - 2 , -1 , -1):
            
            if(arr[i] > currMax) :
                arr[i] , currMax = currMax , arr[i]
            else :
                arr[i] = currMax

        return arr

sol = Solution()
print(sol.replaceElements([17,18,5,4,6,1]))