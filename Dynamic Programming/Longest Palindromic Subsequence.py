# https://www.youtube.com/watch?v=_nCsPn7_OgI

def solution(str) :

    # initialization
    # for single length subsequence, the value will be one
    sol = [[1 if i==j else 0 for i in range(len(str))] for j in range(len(str))]
    maxVal = 1
    

    # movement in the matrix
    for i in range(len(str)-1) :
        
        for j in range(i+1,len(str)) :
            if str[j-i-1] == str[j] :
                sol[j-i-1][j] = sol[j-i][j-1] + 2
                maxVal = maxVal if maxVal > sol[j-i-1][j] else sol[j-i-1][j]
            else :
                sol[j-i-1][j] = max(sol[j-i-1][j-1],sol[j-i][j])

    print("Length of lengest palindromic subsequence is", maxVal)
    


    # printing the longest palindromic subsequence

    index = maxVal
    i, j= 0, len(str)-1
     
    lcs = [""] * (index)
    val = 0  # to fill up the string list from left side
    while (index-val >= 0) :
         
        if sol[i][j-1] == sol[i+1][j] : 
          
            
              
            lcs[index - 1] = str[j]
            lcs[val] = str[j]
             
            i += 1
            j -= 1
            val += 1
              
            index -= 1
              
        elif sol[i][j-1] < sol[i+1][j] : 
            i += 1
              
        else : 
            j -= 1


    ans = "" 
      
    for x in range(len(lcs)) : 
        ans += lcs[x] 

    print("The subsequence is : " +ans)


solution("ACGTGTATGC")
#solution("agbdba")