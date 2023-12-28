# 86) partition list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head, x):
        # similar to quicksort (partition function)
        # qsort(nums, p)
        #   i, j = 0, len(nums)-1
        #   while i <= j:
        #       while nums[i] < x: i += 1
        #       while nums[j] > x: j -= 1
        #       if i < j: swap nums[i] and nums[j]; i += 1, j -= 1 
        left = ListNode(0)
        right = ListNode(0)

        less = left
        greater = right

        curr = head
        
        while curr:
            if curr.val < x: 
                less.next = curr
                less = less.next
            else:
                greater.next = curr
                greater = greater.next

            curr = curr.next

        # combine 2 partitions
        greater.next = None
        less.next = right.next

        return left.next


        
