# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        level = []
        if not root :
            return []
        
        
        queue = [root]
        #queue.append(root)

        while queue:

            next_queue = []
            lst = []
            while queue :
            
                s = queue.pop(0)
                lst.append(s.val)
                if s.left: 
                    next_queue.append(s.left)
                if s.right: 
                    next_queue.append(s.right)
            
            queue = next_queue
            level.append(lst)
        
        return level