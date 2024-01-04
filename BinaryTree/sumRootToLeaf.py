# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root):
        # root: Optional[TreeNode]
        # rtype: int         
        def dfs(node, curr):
            if not node: return 0

            curr = curr * 10 + node.val
            if not node.left and not node.right:
                return curr
            
            return dfs(node.left, curr) + dfs(node.right, curr)

        if root: return dfs(root, 0)
        else: return 0


        # root = [4,9,0,5,1]
        # curr = "4"
        # stack = [4]

        # stack = [4, 9]
        # curr = "4->9->"

        # stack = [4, 9, 5]
        # curr = "4->9->5" append 495 to stack
        # curr = "4->9->1" append 491 to stack
        # curr = "40" append 40 to stack 
        # add all nums in stack

        