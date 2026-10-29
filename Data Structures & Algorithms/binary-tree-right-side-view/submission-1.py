# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # This uses breadth first search using a queue data structure
        queue = collections.deque()
        answer = []

        queue.append(root)
        # At each step of BFS, we only iterate over the queue up to its size at that step. 
        # Then, we take the left and right child pointers and add them to the queue. 
        # This allows us to explore all paths simultaneously.

        # The no. of times we iterate the queue corresponds to the number of levels in the tree.
        # At each step, we pop all nodes from the queue for the current level and add them collectively to the resultant array. 
        # This ensures that we capture all nodes at each level of the tree.
        
        while queue:
            qLen = len(queue)
            rightSide = None
            for i in range(qLen):
                # At each step of BFS, we only iterate over the queue up to its size at that step.
                # we pop all nodes from the queue for the current level and add them collectively to the resultant array. 
                node = queue.popleft()
                if node:
                    # Then, we take the left and right child pointers and add them to the queue exploring all paths simultaneously
                    rightSide = node
                    queue.append(node.left)
                    queue.append(node.right)
            if rightSide:
                # For each level, we only append the rightmost node to the answer
                answer.append(rightSide.val)

        return answer