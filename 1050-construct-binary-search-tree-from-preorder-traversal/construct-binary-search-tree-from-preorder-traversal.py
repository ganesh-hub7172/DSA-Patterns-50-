class Solution:
    def bstFromPreorder(self, preorder):
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]

        for val in preorder[1:]:
            node = TreeNode(val)
            if val < stack[-1].val:
                stack[-1].left = node
            else:
                parent = None
                while stack and stack[-1].val < val:
                    parent = stack.pop()
                parent.right = node
            stack.append(node)

        return root
