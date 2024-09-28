# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """In Trees, either there is a null condition or an action asked to perform in the question. And recursive statements and end Mei ek return statement. This is the Template. Don’t forget to put return root in the null statement if null statement is true."""
        
        if root == None or (root.left==None and root.right==None):
            return root
        else:
            ptr = root.left
            root.left = root.right
            root.right = ptr 
            
        self.invertTree(root.left)
        self.invertTree(root.right)
        #root = invertTree(self, root)
        return root
        