# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # We can use dfs in order traversal so we start with the smallest branch
        # We decrease k for every node we traverse starting from the smallest
        # When k == 0, we store the current node's value in a global variable and return
        res = root.val if root else 0

        def dfs(node):
            nonlocal k, res

            if not node: return

            # left traversal
            dfs(node.left)

            if k == 0: return

            k -= 1 # decrement k
            
            if k == 0:
                res = node.val
                return

            # right traversal
            dfs(node.right)

        dfs(root)
        return res
