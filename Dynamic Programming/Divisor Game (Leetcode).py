

# Without DP solution
'''

class Solution(object):
        
    def divisorGame(self, N):
        if N == 0 or N ==1:
            return False
        
        
        if N%2==0 :
            return True
        else :
            return False

'''
# DP solution
class Solution(object):
        
    def divisorGame(self, N):
        
        dp = [False for i in range(N+1)]
        dp[0] = dp[1] =False

        for i in range(2,N+1) :
            
            if dp[i-1] == False :
                dp[i] = True
            else :
                dp[i] = False 

        return dp[N]


sol = Solution()
print(sol.divisorGame(981))
    