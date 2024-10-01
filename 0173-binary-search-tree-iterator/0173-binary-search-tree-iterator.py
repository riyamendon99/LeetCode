# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):
    
    """LOGIC - There is a stack that pushes in the root and then left node in a loop until no element is present in the left. Then next() function mei topmost elemet gets popped. Now how to do the tree recursion on right side? (Here we can't do recursion and need to solve iteratively. So how will you do the right side?). Answer- When an element is popped from stack, check the right of it an do the same process of pushing the node and then its left node until no element is present in the left. The hasNext() function only checkd if there is any element in the stack or not."""

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        """
        :rtype: int
        """
        ptr = self.stack.pop()
        curr = ptr.right
        while curr:
            self.stack.append(curr)
            curr = curr.left
        return ptr.val #don't forget to return a value
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.stack) == 0:
            return False
        else:
            return True
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()