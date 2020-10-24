# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        
        ans = [root.val]
        nextNodes = [root]
        while nextNodes:
            temp_node = []
            for node in nextNodes:
                if node.left:
                    temp_node.append(node.left)
                if node.right:
                    temp_node.append(node.right)
            if len(temp_node) :
                ans.append(temp_node[-1].val)
            nextNodes = temp_node
        return ans