# 103 - binary tree zigzag level order traversal
# (BFS)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections  # for a live coding interview, always ask if it's ok to use built-in libraries.
class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
                
        curr = root

        q = collections.deque([root])
        ltr = True 
        # left to right pointer, for levels 0, 2, change to false every other level (1, 3, 5)
        
        res = [] 

        while q:
            curr_len = len(q) # 2
            lvl = [None] * curr_len

            for i in range(curr_len):
                node = q.popleft()
                #if curr_len > 1:
                    #q.pop()

                if ltr:
                    idx = i
                else:
                    idx = curr_len - 1 - i
                lvl[idx] = node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(lvl) 
            ltr = not ltr # change flag so next level is rtl (right to left)

        return res


