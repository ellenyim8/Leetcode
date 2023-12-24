# Leetcode 101) Symmetric Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root):
        # dfs recursion
        def dfs(left, right):
            if not left and not right: return True

            if not left or not right or left.val != right.val:
                return False

            # recursion:
            return dfs(left.left, right.right) and dfs(left.right, right.left)


        if root:
            return dfs(root.left, root.right) 
        else: 
            return False
        
        
root = [1,2,2,3,4,4,3]
print(Solution().isSymmetric(root))

root = [1, 2, 2, None, 3, None, 3]
print(Solution().isSymmetric(root))
