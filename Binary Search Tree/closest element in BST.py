import math

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def closestElement(root,k,initialMin,minValue):
    if root == None:
        return minValue
    
    if root.val == k:
        return k
    
    if initialMin > abs(root.val-k):
        initialMin = abs(root.val-k)
        minValue = root.val
    
    if root.val>k:
        return closestElement(root.left,k,initialMin,minValue)
    else:
        return closestElement(root.right,k,initialMin,minValue)


root = TreeNode(9)  
root.left = TreeNode(4)  
root.right = TreeNode(17) 
root.left.left = TreeNode(3)  
root.left.right = TreeNode(6) 
root.left.right.left = TreeNode(5)  
root.left.right.right = TreeNode(7)  
root.right.right = TreeNode(22) 
root.right.right.left = TreeNode(20) 

print(closestElement(root,4,math.inf,-9999999))