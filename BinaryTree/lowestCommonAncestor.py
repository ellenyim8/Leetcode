# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or root.val == p.val or root.val == q.val:
            return root

        # search for LCA in left subtree
        left = self.lowestCommonAncestor(root.left, p, q)
        # search for LCA in right subtree
        right = self.lowestCommonAncestor(root.right, p, q)
        # if left and right then  return root
        if left and right:
            return root
        # return left if left else right
        return left if left else right

        