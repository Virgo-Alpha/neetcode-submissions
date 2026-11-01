# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # We can use dfs in order traversal so we start with the smallest branch
        # We keep a counter variable cnt to track the position of the current node in the ascending order of values.
        # When cnt == k, we store the current node's value in a global variable and return
        cnt = 0
        res = root.val if root else 0

        def dfs(node):
            nonlocal cnt, res

            # 1. Base Case: If the node doesn't exist, stop and turn back
            if not node: return

            if cnt == k: return node.val
            
            # 2. Left Step: Explore the entire left subtree first
            dfs(node.left)
            
            # 3. Current Step: "Visit" and process the current node here
            # The counter logic and k-check belong here
            cnt += 1

            if cnt == k:
                res = node.val
            
            # 4. Right Step: Explore the entire right subtree last
            dfs(node.right)

            return res
            

        return dfs(root)
