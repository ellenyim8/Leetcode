# 21) Merge 2 Sorted (Linked) Lists

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        if not list1 and list2:
            return list2

        if list1 and not list2:
            return list1 
            
        dummy = ListNode(-1)
        curr = dummy 

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1:
            curr.next = list1
        else:
            curr.next = list2

        return dummy.next
    
    

list1 = [1,2,4]
list2 = [1,3,4]
print(Solution().mergeTwoLists(list1, list2))

