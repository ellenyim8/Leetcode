# REmove duplicates from sorted list II

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        if not head or not head.next: return head

        right = ListNode(0)
        right.next = head
        left = right
        
        while head:
            while head.next and head.val == head.next.val:
                head = head.next

            if left.next == head:
                left = left.next
            else:
                left.next = head.next # remove nodes from duplicates

            head = head.next

        return right.next



        