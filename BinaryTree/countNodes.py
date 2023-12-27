# 222) Count complete tree nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root) -> int:
        cnt = 0
        if not root: return 0

        left = self.countNodes(root.left)
        right = self.countNodes(root.right)

        return 1 + left + right # 1 is counting the root
        
    