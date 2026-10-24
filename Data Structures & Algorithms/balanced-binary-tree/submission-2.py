# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root: return 0
            
            # 1. Check the left subtree
            left_height = dfs(root.left)
            if left_height == -1: 
                return -1  # Short-circuit: stop checking and pass the failure up
            
            # 2. Check the right subtree
            right_height = dfs(root.right)
            if right_height == -1: 
                return -1  # Short-circuit: stop checking and pass the failure up
            
            # 3. Check the current node
            if abs(left_height - right_height) > 1:
                return -1  # Current node is unbalanced
            
            # Subtree is balanced; return its actual height
            return 1 + max(left_height, right_height)

        # If it returns -1, the tree is unbalanced. Otherwise, it's balanced.
        return dfs(root) != -1
