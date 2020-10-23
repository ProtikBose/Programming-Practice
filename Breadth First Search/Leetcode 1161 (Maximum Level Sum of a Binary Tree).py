# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
            
    
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sumLevel = [0]*100
        
        
        def traverse(root,level):
            
            sumLevel[level] += root.val
            if root.left:
                traverse(root.left,level+1)
            if root.right:
                traverse(root.right,level+1)
                
        traverse(root,0)
        return sumLevel.index(max([item for item in sumLevel if item !=0 ]))+1
        