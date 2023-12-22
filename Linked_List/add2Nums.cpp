// 2) Add 2 numbers
#include <iostream>
using namespace std;

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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        /* 
        1. Traverse two linked lists.
        2. In each iteration, add the numbers in the nodes of the linked lists
        3. If the lists are unequal, then the smaller one will end before the longer. In this           case, we will put only the remaining nodes of the longer list in the resultant list
        4. If the sum of two digits is greater than 9, then we will have to find out the                “carry” to be added in the next iteration.
        */
        int sum; 
        ListNode* head = NULL; 
        ListNode* temp = NULL; 
        int carry = 0;
        
        while (l1 != NULL || l2 != NULL) {
            // at start of each iteration, add carry from last iteration. 
            sum = carry; 
            // Since the lengths of the lists may be unequal, we are checking if the
            //current node is null for one of the lists
            if (l1 != NULL) {
                sum += l1->val; 
                l1 = l1->next;
            }
            if (l2 != NULL) {
                sum += l2->val; 
                l2 = l2->next; 
            }
            
            // now we add total sum % 10 to new node in result list
            ListNode* add = new ListNode(sum % 10);
            // carry to be added in next iteration 
            carry = sum / 10; 
            // if first node or head
            if (temp == NULL) {
                temp = head = add; 
            }
            // else - any other node
            else {
                temp->next = add; 
                temp = temp->next; 
            }
            
        }
        // After the last iteration, we will check if there is carry left
        // If it's left then we will create a new node and add it
        if (carry > 0) {
            temp->next = new ListNode(carry);
            
        }
        return head; 
    }
};
