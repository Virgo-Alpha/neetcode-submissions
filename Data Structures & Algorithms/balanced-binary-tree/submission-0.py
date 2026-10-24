# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # We can use the Depth First Search (DFS) algorithm to compute the heights at each node.
        # While calculating the heights of the left and right subtrees, 
        # we also check if the tree rooted at the current node is balanced. 
        # If leftHeight - rightHeight > 1, we update a global variable, 
        # such as isBalanced = False. 
        # After traversing all the nodes, the value of isBalanced indicates 
        # whether the entire tree is balanced or not.

        isBalanced = True

        def dfs(node):
            # Base case
            if not node: return 0

            # nonlocal: Python keyword used inside a nested function to modify a variable defined in the outer function
            nonlocal isBalanced

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            if right_height - left_height > 1 or left_height - right_height > 1:
                isBalanced = False

            # determine the height
            return 1 + max(left_height, right_height)

        dfs(root)

        return isBalanced
