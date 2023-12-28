# 61) Rotate List (right)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head, k) :
        if k == 0 or head == None: return head
        l = 1

        # find length of list
        curr = head
        while curr.next:
            curr = curr.next 
            l += 1
        
        # connect last node with head to make a cycle
        curr.next = head 

        k = k % l # actual # of rotations

        for _ in range(l - k - 1):
            head = head.next

        tmp = head.next
        head.next = None
            
        return tmp
        
