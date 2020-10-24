# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        
        nextNodes = [root]
        maxValue = [root.val]
        
        while nextNodes:
            temp_node = []
            for node in nextNodes:
                if node.left:
                    temp_node.append(node.left)
                if node.right:
                    temp_node.append(node.right)
            if len(temp_node) :
                maxValue.append( max([item.val for item in temp_node]))
            nextNodes = temp_node
        return maxValue