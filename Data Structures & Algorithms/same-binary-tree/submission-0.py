# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # We can use the Depth First Search (DFS) algorithm to traverse the tree. 

        # We traverse both trees starting from their root nodes. 
        # At each step in the recursion, we check if the current nodes in both trees are either null or have the same value. 
        # If one node is null while the other is not, or if their values differ, we return false. 
        # If the values match, we recursively check their left and right subtrees. If any recursive call returns false, the result for the current recursive call is false.

        def dfs(tree_1, tree_2):
            # when both are null
            if not tree_1 and not tree_2: return True

            # when Both have the same value
            elif tree_1 and tree_2 and tree_1.val == tree_2.val:
                # recursively check their left and right subtrees
                return dfs(tree_1.left, tree_2.left) and dfs(tree_1.right, tree_2.right)
            else:
                return False

        return dfs(p, q)

