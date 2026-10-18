# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Use a single while loop and a new list

        # 1. Keep a single pointer (let's call it curr) starting at your ListNode(0) dummy head to build your new list step-by-step.
        # 2. Track a single carry integer (initially 0) outside the loop.
        # 3. Run one loop that keeps going as long as l1 is alive, OR l2 is alive, OR carry is greater than 0.
        # 4. Inside the loop:
        # • Get the value from l1 (if it exists, otherwise 0).
        # • Get the value from l2 (if it exists, otherwise 0).
        # • Calculate the total = val1 + val2 + carry.
        # • Update your carry for the next round (total // 10).
        # • Create a new node with just the digit value (total % 10) and attach it to curr.next.
        # • Advance your pointers (l1, l2, and curr) forward.

        curr = dummy = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            # get the 2 values or 0
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            total = l1_val + l2_val + carry

            carry = total // 10

            curr.next = ListNode(total % 10)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next if curr else None

        return dummy.next
