# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def increasingBST(self, root):
        stack = []
        cur = root
        dummy = TreeNode(0)
        tail = dummy
        
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            cur.left = None
            tail.right = cur
            tail = cur
            cur = cur.right
        
        return dummy.right
