class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) <= 2 :
            return False
        
        i = 0
        N = len(A)

        while i+1 < N and A[i]< A[i+1] :
            i += 1

        if i == 0 or i == N-1 :
            return False

        while i+1 < N and A[i] > A[i+1] :
            i += 1

        if i == N-1 :
            return True
        else :
            return False

            
        return True