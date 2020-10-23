class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix)==0 or len(matrix[0])==0:
            return []
        row = len(matrix)
        column = len(matrix[0])
        
        upward = True
        i = 0
        j = 0
        visited = row*column
        outputList = []
        
        while(visited):
            
            if upward :
                while i>=0 and j<column:
                    outputList.append(matrix[i][j])
                    visited -= 1
                    i-=1
                    j+=1
                
                #row crossed
                if i<0 and j<=column-1: 
                    i = 0
                #corner
                if j==column: 
                    i+=2
                    j-=1
                    
            else:
                while j>=0 and i<row:
                    outputList.append(matrix[i][j])
                    visited -= 1
                    i+=1
                    j-=1
                
                #column crossed
                #row crossed
                if j<0 and i<=row-1: 
                    j = 0
                #corner
                if i==row: 
                    j+=2
                    i-=1
            upward = not upward
        return outputList
        