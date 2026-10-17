"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # We can use a hash map, which takes O(1) time to retrieve data. 
        # This can help by mapping the original nodes to their corresponding copies. 
        # This way, we can easily retrieve the copy of any node and assign the random pointers in a subsequent pass after creating copies of all nodes in the first pass.

        oldToCopy = {None: None} # old: copy

        cur = head
        while cur:
            # first loop for new node to old node
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            # second loop for next and random pointers
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]

