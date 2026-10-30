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
        answer = 0 # a count of good nodes

        def dfs(node, max_val=0):
            if not node: return

            nonlocal answer

            current_value = node.val

            if current_value >= max_val:
                # This will count the root node
                answer += 1
                max_val = current_value
            
            # How then do we traverse left and right children of the node?
            if node.left:
                dfs(node.left, max_val)
            if node.right:
                dfs(node.right, max_val)

            return

        dfs(root, root.val)

        return answer
