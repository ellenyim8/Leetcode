// 19) Remove Nth node from End of List
#include <iostream>

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
 
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* pre = new ListNode(0, head), *cur = pre, *post = pre;

        while (post->next != nullptr && n-- > 0) post = post->next; 

        while (post->next != nullptr) {
            post = post->next; 
            cur = cur->next; 
        }
        cur->next = cur->next->next;
        return pre->next; 
    }
};
