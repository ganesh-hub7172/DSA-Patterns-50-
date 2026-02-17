class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        
        left_root = preorder[1]
        k = postorder.index(left_root) + 1
        
        root.left = self.constructFromPrePost(preorder[1:1+k], postorder[:k])
        root.right = self.constructFromPrePost(preorder[1+k:], postorder[k:-1])
        return root
