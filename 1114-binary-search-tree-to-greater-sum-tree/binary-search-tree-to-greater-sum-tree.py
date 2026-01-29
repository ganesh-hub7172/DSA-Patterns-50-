# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root):
        self.total = 0

        def dfs(node):
            if not node:
                return

            # Visit right subtree first
            dfs(node.right)

            # Update sum and node value
            self.total += node.val
            node.val = self.total

            # Visit left subtree
            dfs(node.left)

        dfs(root)
        return root
