# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # change from ordered to [0, n-1, 1, n-2, 2, n-3, ...]

        # We can divide the list into two halves using the l2 and l1 pointers approach,  
        # ? which helps identify the midpoint of the list. 
        # This allows us to split the list into two halves, with the heads labeled l1 & l2.
        # we reverse the second half (l2). 
        # After these steps, we proceed to reorder the two lists by iterating through them node by node, updating the next pointers accordingly.

        # The trick is the 3 loops needed to split into 2, reverse the second half and merge with the first
        if not head or not head.next:
            return

        l1, l2 = head, head.next

        while l2 and l2.next:
            # loop 1: split into 2 and severe them from each other
            l1 = l1.next
            l2 = l2.next.next

        # at the end of the loop sever the 2 halves
        second = l1.next
        l1.next = None  # This cleanly severs the first half from the second half
        prev = None     # Initialize prev to None for our reversal loop

        
        # loop 2: reverse from the midpoint which will be l1
        while second:
            # store the next node
            tmp = second.next

            # l2.next becomes prev, prev becomes current node
            second.next, prev = prev, second

            # move to next node till the end
            second = tmp

        # prev is now the head of l2

        # Now we need to merge l1 and prev
        first, second = head, prev

        # loop 3: merge the 2 linkedlists
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

