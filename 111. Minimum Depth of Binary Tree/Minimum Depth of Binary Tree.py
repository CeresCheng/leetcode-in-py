# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
        if root is None:
            return 0
        elif root.left is None or root.right is None:
            return self.minDepth(root.left) + self.minDepth(root.right) + 1
        else:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
