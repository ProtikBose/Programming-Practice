
class Node(object):
    
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

'''
# BFS -----> O(n)
class Solution(object):
    
    def maxDepth(self, root):
        if not root :
            return 0
        
        maxDepth = 0
        queue = [root]
        #queue.append(root)

        while queue:

            next_queue = []
            while queue :
            
                s = queue.pop(0)
                if s.children: 
                    next_queue.extend(s.children)
            
            queue = next_queue 
            maxDepth += 1        

        return maxDepth
'''

# DFS -----> O(n)

class Solution(object):
    
    def maxDepth(self, root):
        
        if not root:
            return 0
        
        max_depth = 1
        if root.children:
            for c in root.children:
                max_depth = max(max_depth, self.maxDepth(c) + 1)

        return max_depth

#root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
root = Node(1,[Node(3,[Node(5),Node(6)]),Node(2,None),Node(4,None)])
sol =Solution()
print(sol.maxDepth(root))

    
        