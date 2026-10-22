# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # If root is None, depth is 0 (no nodes)
        # If root exists with no children, depth is 1 (one node)

        # Base case: empty tree has depth 0
        if not root: return 0

        # we add the root node to the recursive call made on its longest child
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
