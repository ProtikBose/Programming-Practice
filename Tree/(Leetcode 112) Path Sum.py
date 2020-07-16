#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        
        
        def recursive(root,total,flag) :
            
            if not root :
                print("Hi")
                return 
            print("Value :",root.val)
            print("Value Left :",root.left)    
            print("Total :",total)
            print()
            if root.left is None and root.right is None :
                
                if sum == total+root.val :
                    print("Ok")
                    flag[0] = True
                
            
            recursive(root.left,total+root.val,flag)
            recursive(root.right,total+root.val,flag)
        
        
        flag = [False]    
        recursive(root,0,flag)
        return flag[0]
            

tree = TreeNode(5,TreeNode(4,TreeNode(11),None),TreeNode(8,TreeNode(13),TreeNode(14)))            
sol = Solution()
print(sol.hasPathSum(tree,20))