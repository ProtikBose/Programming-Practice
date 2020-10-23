class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxHeight(root,height):
    if root == None:
        return height
    
    return max(maxHeight(root.left,height+1),maxHeight(root.right,height+1))

root = TreeNode(5)  
root.left = TreeNode(1)  
root.right = TreeNode(4) 
root.right.left = TreeNode(3)  
root.right.right = TreeNode(6) 



print(maxHeight(root,0))