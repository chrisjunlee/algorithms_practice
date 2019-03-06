# no parent or height
class Solution:
    # cascading isolation technique
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q:
            return root

        res_left, res_right = None, None

        # recurse left/right
        if root.left:
            res_left = self.lowestCommonAncestor(root.left, p, q)

        if root.right:
            res_right = self.lowestCommonAncestor(root.right, p, q)

        # if left and right returns: we are the LCA
        if res_left and res_right:
            return root

        # if only one. answer is the bubbled up child result
        return res_left if res_left else res_right
