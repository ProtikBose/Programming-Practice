# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nextNodes = [root]
        currLeft = root.val
        while nextNodes:
            temp_node = []
            for node in nextNodes:
                if node.left:
                    temp_node.append(node.left)
                if node.right:
                    temp_node.append(node.right)
            if len(temp_node) :
                currLeft = temp_node[0].val
            nextNodes = temp_node
        return currLeft