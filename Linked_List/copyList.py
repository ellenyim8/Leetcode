# 138) Copy list with random pointer

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        copy = {None : None}

        curr = head

        # create copies of each node, traverse the list
        # create mapping from each node of list to node of new list
        while curr:
            node = Node(curr.val)
            copy[curr] = node
            curr = curr.next

        # traverse head list again, copy next and random pointer to new list
        curr = head

        while curr:
            node = copy[curr]
            node.next = copy[curr.next]
            node.random = copy[curr.random]
            curr = curr.next

        # return first value of hashmap - storing head of deep copy
        return copy[head]

        # Evaluate: 
        # Time: O(n), Space: O(n) 
        

        
