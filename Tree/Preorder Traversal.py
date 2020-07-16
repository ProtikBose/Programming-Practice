# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ''' 
        def recursive(root) :
            if not root :
                return
        
            lst.append(root.val)
        
            recursive(root.left)
            recursive(root.right)
        
        lst = []
        recursive(root)
        return lst
        
        '''

        def iterative(root) :
            
            if not root :
                return []
            stack = [root]
            out = []
            
            while len(stack) :
                
                temp = stack.pop()
                out.append(temp.val)

                # we are popping...    
                if temp.right :
                    stack.append(temp.right)
                if temp.left :
                    stack.append(temp.left)
                    
            return out
        
        return iterative(root) 