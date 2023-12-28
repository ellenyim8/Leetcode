# 106) Convert Binary Tree from inorder and postorder traversal

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder, postorder):
        # inorder: left, root, right
        # postorder: left, right, root
        if not inorder or not postorder:
            return None
        
        # last node of postorder is the root
        #root = TreeNode(postorder[-1])
        
        n = len(inorder)

        stack = [] # stack  
        set = []     # set

        post_idx = n - 1
        root = None
        p = n - 1
        i = n - 1

        while p >= 0:
            node = None

            while True:
                # init new node
                node = TreeNode(postorder[p])
                if root == None:
                    root = node

                if len(stack) > 0:
                    # If st top is present in the set s
                    if stack[-1] in set:
                        set.remove(stack[-1])
                        stack[-1].left = node
                        stack.pop()
                    else:
                        stack[-1].right = node

                stack.append(node)

                p -= 1
                if postorder[p + 1] == inorder[i] or p < 0:
                    break
                
            node = None

            # If the stack is not empty and st top data is equal to in[i]
            while len(stack) > 0 and i >= 0 and stack[-1].val == inorder[i]:
                node = stack[-1]
                stack.pop()
                i -= 1

            if node != None:
                set.append(node)
                stack.append(node)

        return root



        
