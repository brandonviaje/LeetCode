/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

class Solution {
public:
    bool hasCycle(ListNode *head) {
        /*
            Floyd Cycle Detection 

            Proof:
            - Suppose there is a cycle of length k.
            - Both slow and fast pointers will eventually enter the cycle.
            - Once inside, their positions can be viewed modulo k (like a circular array).
            - On each iteration, fast moves 2 steps and slow moves 1 step, so fast gains 1 step per round.
            - Therefore, they must meet within at most k steps (by modular arithmetic).

            - If there is no cycle:
              - fast will reach the end, and the loop exits.
        */

        ListNode* slow = head;
        ListNode* fast = head;

        // ensure fast and fast->next are not null to safely advance fast by two steps without seg fault
        while (fast && fast->next) {
            //fast moves two nodes ahead, slow moves one node only
            slow = slow->next;
            fast = fast->next->next;

            if (slow == fast) {
                return true; // cycle detected
            }
        }

        return false;

        // T O(n) S O(1)
    }
};
