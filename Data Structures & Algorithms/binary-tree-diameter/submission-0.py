# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        We can use the Depth First Search (DFS) algorithm to calculate the height of the tree. 
        At each node, the subtrees return their respective heights (leftHeight and rightHeight). 
        Then we calculate the diameter at that node as d = leftHeight + rightHeight. 
        We use a global variable to update the maximum diameter as needed during the traversal.
        """
        self.max_d = 0  # Use an instance variable to track the max diameter globally

        def get_height(node):
            if not node: return 0
            
            # Recursively find the height of left and right subtrees
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            
            # The diameter at the current node is the sum of left and right heights
            current_diameter = left_height + right_height
            
            # Update the global maximum diameter found so far
            self.max_d = max(self.max_d, current_diameter)
            
            # Return the height of the current node to its parent
            return max(left_height, right_height) + 1

        get_height(root)
        return self.max_d

        