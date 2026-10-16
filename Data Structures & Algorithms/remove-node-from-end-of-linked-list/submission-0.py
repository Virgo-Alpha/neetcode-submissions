# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # We can use a two-pass approach by first finding the length of the list, N. 
        # Since removing the nth node from the end is equivalent to removing the (N - n)th node from the front, as they both mean the same. How can you remove the node in a linked list?

        # We can avoid a separate length-counting pass with two pointers. 
        # Move the first pointer n steps ahead from the head. 
        # Then, start another pointer second at a dummy node before the head and iterate both pointers simultaneously until first reaches null. 
        # At this point, the second pointer is just before the node to be removed. We then remove the node that is next to the second pointer.

        # This works because first stays n nodes ahead of second.next. When first reaches the end, second.next is exactly the nth node from the end. This positioning allows us to remove that node efficiently.
        first, second = head, ListNode()
        second.next = first
        answer = second

        while n:
            first = first.next
            n -= 1
        
        while first:
            first, second = first.next, second.next

        second.next = second.next.next

        return answer.next

