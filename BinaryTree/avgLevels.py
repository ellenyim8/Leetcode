# 637) average of levels in binary tree 
# BFS
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root):
        if not root: return []
        # bfs
        q = collections.deque([root])
        # first level: 3 - avg (3 / 1 = 3.0000)
        # second level: (9 + 20) / 2 = 29 / 2 = 14.5000
        # third level: (15 + 7) / 2 = 22 / 2 = 11 

        avgs = []

        while q:
            lvl_sum = 0
            lvl_cnt = 0
            q_len = len(q)

            for i in range(q_len):
                node = q.popleft()
                lvl_sum += node.val
                lvl_cnt += 1

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            avgs.append(lvl_sum / lvl_cnt)

        return avgs

        
