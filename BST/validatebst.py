# 98 - validate binary search tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
INT_MIN = pow(-2, 31)
INT_MAX = pow(2, 31) - 1

class Solution:
    def isValidBST(self, root):
        def helper(root, minval, maxval):
            if root is None: return True

            if root.val < minval or root.val > maxval: return False

            return helper(root.left, minval, root.val-1) and helper(root.right, root.val+1, maxval)

        return helper(root, INT_MIN, INT_MAX)

