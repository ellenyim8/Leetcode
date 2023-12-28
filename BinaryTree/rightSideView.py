# 199) binary tree right side view
# BFS 
import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        
        # bfs 
        right = []

        q = collections.deque([root])

        while q:
            right_side = None
            q_len = len(q)

            for i in range(q_len):
                node = q.popleft()
                if node:
                    right_side = node
                    q.append(node.left)
                    q.append(node.right)
    
            if right_side:
                right.append(right_side.val)
        
        return right

        
