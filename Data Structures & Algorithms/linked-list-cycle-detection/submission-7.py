# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # use 2 pointers: 1 fast, 1 slow
        # The fast one moves 2 steps at once, the slow one moves node by node

        if head and head.next:
            slow, fast = head, head.next
        else:
            return False

        while fast and fast.next:
            if fast == slow:
                return True
            slow = slow.next

            if fast.next:
                fast = fast.next.next 
            else:
                return False

        return slow == fast