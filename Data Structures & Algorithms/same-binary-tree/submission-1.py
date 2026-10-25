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

        # We do not need a nested function

        if not p and not q: return True
        
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

