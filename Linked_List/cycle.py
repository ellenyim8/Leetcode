# 141) Linked list cycle 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        if not head or not head.next: return False

        # keep fast pointer ahead of slow by 2 
        slow = head
        fast = head.next.next

        while slow != fast:
            if not fast or not fast.next: # reached end, no cycles
                return False
            slow = slow.next      # slow pointer 1 step ahead
            fast = fast.next.next # fast pointer go 2 steps ahead

        return True

        
