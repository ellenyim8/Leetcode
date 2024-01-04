# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root):
        # root: Optional[TreeNode] 
        # rtype: int
        def helper(node):
            nonlocal max_sum
            if not node: return 0
            # calculate left and right subtree sums
            left_sum = max(0, helper(node.left))
            right_sum = max(0, helper(node.right))
            # update max_sum by considering current node's val
            max_sum = max(max_sum, left_sum + right_sum + node.val)
            # return maximum path sum starting from current node
            return max(left_sum, right_sum) + node.val

        max_sum = float('-inf')
        helper(root)
        return max_sum
    