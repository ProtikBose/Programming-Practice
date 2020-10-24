"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        
        answer = []
        children,nextnodes = [],[root]
        while nextnodes:
            temp_children = []
            temp_nodes = []
            for node in nextnodes:
                temp_children.append(node.val)
                for child in node.children:
                    temp_nodes.append(child)
            nextnodes = temp_nodes
            answer.append(temp_children)
        return answer
        