class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        
        # easy solution
        '''
        i = 0
        n = len(arr)
        
        while i < n :
            if arr[i] == 0:
                arr.insert(i+1,0)
                i += 2
            else:
                i +=1 
        del arr[n:len(arr)]       
        
        '''    

        # O(n) time and O(1) space
        # https://leetcode.com/articles/duplicate-zeros/

        possible_change = 0
        length = len(arr) - 1

        for i in range(length + 1) :

            if i > length - possible_change :
                break

            if arr[i] == 0 :
                # for corner case
                if i == length - possible_change :
                    arr[length] = 0
                    length -= 1
                    break
                possible_change += 1

        last = length - possible_change

        for i in range(last,-1,-1) :
            if arr[i] == 0 :
                arr[i + possible_change] = 0
                arr[i + possible_change - 1] = 0
                possible_change -= 1
            else :
                arr[i + possible_change] = arr[i]