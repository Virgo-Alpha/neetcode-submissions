# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        # The first next will be node coz head turns to tail
        prev = None

        while head:
            # store the next node
            next_node = head.next

            # head.next becomes prev, prev becomes current node
            head.next, prev = prev, head

            # move to next node till the end
            head = next_node

        return prev  # because at the end, head is None due to how the loop ends
