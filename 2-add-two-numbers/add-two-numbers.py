# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1Str = ""
        l2Str = ""
        curr = ListNode()
        head = curr
        # build l1 and l2 string by prepending
        while l1:
            l1Str = str(l1.val) + l1Str 
            l1 = l1.next

        while l2:
            l2Str = str(l2.val) + l2Str 
            l2 = l2.next

        # add em together type cast to string, and reverse
        num1 = int(l1Str)
        num2 = int(l2Str)
        add = num1 + num2
        reverse = str(add)[::-1]
        
        for c in reverse:
            curr.next = ListNode(int(c))
            curr = curr.next

        return head.next
        