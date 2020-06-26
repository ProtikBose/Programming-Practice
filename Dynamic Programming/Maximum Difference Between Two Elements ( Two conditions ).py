# Ref : https://youtu.be/SO0bwMziLlU

# largest number appears after small number

##########################################################################

# Without DP solution
'''

Time Comp : O(n)
Space Comp : O(1)

Method : keep track of -

1) Find maximum difference so far
2) Find current minimum so far

def solution(lst) :

    if len(lst) == 0 or len(lst) == 1 :
            return 0

    max_diff = lst[1] - lst[0]
    curr_min = lst[0]

    for i in range(1,len(lst)) :
        if lst[i] - curr_min > max_diff :
            max_diff = lst[i] - curr_min
        if lst[i] < curr_min :
            curr_min = lst[i]
    
    if max_diff <= 0 :
        return 0
    return max_diff

print(solution([80, 2, 6, 3, 100]))

'''

# DP Solution

'''

Time Comp : O(n)
Space Comp : O(n)

Method : keep track of -

1) Find temporary difference for adjacent elements
2) Do maximum sum subarray 


def solution(lst) :
    
    dp = [0] * (len(lst)-1)
    for i in range(len(lst)-1) :
        dp[i] = lst[i+1]-lst[i]

    max_diff = dp[0]

    for i in range(1,len(lst)-1) :
        if dp[i-1] > 0 :
            dp[i] += dp[i-1]
        if max_diff < dp[i] :
            max_diff = dp[i]

    return max_diff

print(solution([80, 2, 6, 3, 100]))

'''

###########################################################################################################

# smaller element appears after the large one
# just inverse approach

def solution(lst) :

    if len(lst) == 0 or len(lst) == 1 :
            return 0

    max_diff = lst[0] - lst[1]
    curr_min = lst[0]

    for i in range(1,len(lst)) :
        if  curr_min - lst[i]  > max_diff :
            max_diff = curr_min - lst[i]
        if lst[i] > curr_min :
            curr_min = lst[i]
    
    if max_diff <= 0 :
        return 0
    return max_diff

print(solution([80, 2, 6, 3, 100]))
print(solution([1, 2, 90, 10, 110]))