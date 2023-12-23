# Leetcode 100) Same Tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p, q):
        # rtype: bool 
        # p : TreeNode
        # q : TreeNode 

        if not p and not q: return True # case if both empty trees

        if not p or not q: return False # if one tree is empty

        if p.val != q.val: return False

        # recursion: check left and right nodes
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        
        