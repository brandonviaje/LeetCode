# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        one thing you can do is compare each node from the list
        whatever is the smallesst you add to the result list
        if one runs out, add the rest of the other list
        """

        result = ListNode()
        head = result

        while list1 and list2:
            # check if list1 has smallest node
            if list1.val < list2.val:
                result.next = ListNode(list1.val)
                list1 = list1.next
                result = result.next
            else:
                result.next = ListNode(list2.val)
                list2 = list2.next
                result = result.next

        # add leftovers if any
        while list1:
            result.next = ListNode(list1.val)
            list1 = list1.next
            result = result.next

        while list2:
            result.next = ListNode(list2.val)
            list2 = list2.next
            result = result.next

        return head.next