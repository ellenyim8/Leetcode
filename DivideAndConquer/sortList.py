# 148) Sort list 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head):
        if head == None or head.next == None:
            return head

        slow = head
        fast = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        mid = slow
        nextMid = mid.next

        mid.next = None

        left = self.sortList(head)
        right = self.sortList(nextMid)

        res = self.sortedMerge(left, right)
        return res

    def sortedMerge(self, left, right):
        res = None
        if left == None: return right
        if right == None: return left

        if left.val < right.val:
            res = left
            res.next = self.sortedMerge(left.next, right)
        else:
            res = right
            res.next = self.sortedMerge(left, right.next)

        return res




