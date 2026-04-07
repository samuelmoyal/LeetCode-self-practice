# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        out=[]
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        if root.left and not root.right:
            return self.inorderTraversal(root.left)+[root.val]
        if not root.left and root.right:
            return [root.val]+self.inorderTraversal(root.right)

        if root.left and root.right:
            return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)


        
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        