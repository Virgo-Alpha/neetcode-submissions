# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        We use recursion and the sorted properties of a binary search tree
        """
        if not root or not p or not q: return None
        
        if root.left and (max(p.val, q.val) < root.val):
            # Move left only if the greater value is smaller than root.val
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.right and (min(p.val, q.val) > root.val):
            # Move right only if the smaller value larger than root.val.
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            # the paths split (or you hit one of the nodes)
            # If the paths split then the current node is the LCA
            # The same is true if you hit one of the nodes
            return root
