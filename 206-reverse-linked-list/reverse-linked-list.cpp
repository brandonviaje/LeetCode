/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {

        //change pointers direction
        ListNode* previous = nullptr;
        ListNode* current = head;

        //iterate till current is empty
        while(current){
            ListNode* temp = current->next;
            current->next = previous;
            previous = current;
            current = temp;
        }

        //previous becomes the new head
        return previous;

        //T O(n) S O(1)
        // most optimal
    }
};