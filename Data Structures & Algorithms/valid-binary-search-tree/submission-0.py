# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #  We can use dfs
        # One famous mistake is the -ve values in the nodes

        def dfs(node, low, high):

            if not node: return True

            if low < node.val < high:
                return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
            return False

        return dfs(root, float('-inf'), float('inf'))