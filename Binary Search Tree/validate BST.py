# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    
    def validBST(self,root,leftNode,rightNode):
        if root == None:
            return True
        if not (leftNode<root.val and root.val<rightNode):
            return False
        
        return self.validBST(root.left,leftNode,root.val) and self.validBST(root.right,root.val,rightNode)
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.validBST(root,float("-inf"),float("inf"))
    
    