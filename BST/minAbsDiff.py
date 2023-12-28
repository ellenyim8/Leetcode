# 530 - minimum absolute difference in BST


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root):
        inorder = []

        def inorderTraverse(inorder, root):
            if not root:
                return

            inorderTraverse(inorder, root.left)
            inorder.append(root.val)
            inorderTraverse(inorder, root.right)

        inorderTraverse(inorder, root)
        min_diff = float('inf')
        n = len(inorder)

        for i in range(n - 1):
            min_diff = min(min_diff, abs(inorder[i + 1] - inorder[i]))
        
        return min_diff

        
