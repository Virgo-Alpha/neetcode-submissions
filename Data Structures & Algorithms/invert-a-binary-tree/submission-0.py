# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Recommended space and time complexity O(n)
        # The left and right children of every node in the tree are swapped

        if not root: return None
        
        # We can use the Depth First Search (DFS) algorithm
        # # This inverts the current node, but every node in the tree also needs to be inverted.
        root.left, root.right = root.right, root.left
         
        # To achieve this, we recursively visit the left and right children and perform the same operation. If the current node is null, we simply return.
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root