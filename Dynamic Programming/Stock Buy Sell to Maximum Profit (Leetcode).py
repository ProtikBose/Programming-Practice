# https://youtu.be/JaosdXkUWTs

# similar as "Maximum Difference Between Two Elements"

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # without dp solution
        if len(prices) == 0 or len(prices) == 1 :
            return 0
        
        max_diff = prices[1] - prices[0]
        curr_min = prices[0]

        for i in range(1,len(prices)) :
            if prices[i] - curr_min > max_diff :
                max_diff = prices[i] - curr_min
            if prices[i] < curr_min :
                curr_min = prices[i]
        if max_diff <= 0 :
            return 0
        return max_diff

        # dp solution
        '''
        if len(prices) == 0 or len(prices) == 1 :
            return 0
        dp = [0] * (len(prices)-1)
        for i in range(len(prices)-1) :
            dp[i] = prices[i+1]-prices[i]

        max_diff = dp[0]

        for i in range(1,len(prices)-1) :
            if dp[i-1] > 0 :
                dp[i] += dp[i-1]
            if max_diff < dp[i] :
                max_diff = dp[i]
        if max_diff <= 0 :
            return 0 
        return max_diff
        '''