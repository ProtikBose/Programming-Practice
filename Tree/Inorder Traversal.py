# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        '''
        def recursion(root) :
            
            if not root:
                return
            
            recursion(root.left)
            lst.append(root.val)
            recursion(root.right)
        
        lst = []
        recursion(root)
        return lst
        
        '''
        
        def iterative(root) :
            
            if not root :
                return []
            stack = []
            out = []
            current = root
            
            while 1 :
                
                if current :
                    stack.append(current)
                    current = current.left

                elif len(stack):
                    current = stack.pop()
                    out.append(current.val)
                    current = current.right
                    
                else :
                    break
                    
            return out
        
        return iterative(root) 