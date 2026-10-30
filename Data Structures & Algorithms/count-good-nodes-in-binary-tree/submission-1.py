# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # we can use dfs for this
        # While traversing the tree, we should track the maximum value along the current path.
        # This allows us to determine whether the nodes we encounter are good. 
        # We can use a global variable to count the number of good nodes.

        def dfs(node, max_val):
            if not node: return 0
            
            # a count of good nodes
            answer = 1 if node.val >= max_val else 0

            max_val = max(max_val, node.val)

            answer += dfs(node.left, max_val)
            answer += dfs(node.right, max_val)
            
            return answer

        return dfs(root, root.val)
