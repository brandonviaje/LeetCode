# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        track = []
        #add all values in linked list
        while head:
            track.append(head.val)
            head = head.next

        dummy = ListNode()
        current = dummy
        
        while track:
            current.next = ListNode(track.pop())
            current = current.next

        return dummy.next