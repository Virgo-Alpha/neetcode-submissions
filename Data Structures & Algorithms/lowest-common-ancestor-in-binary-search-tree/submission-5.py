# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """We use recursion and the sorted properties of a binary search tree"""
        if not root: return None
        
        if root.left and root.val > p.val and root.val > q.val:
            # Move left only if both p.val and q.val are smaller than root.val
            root = root.left
        elif root.right and root.val < p.val and root.val < q.val:
            # Move right only if both p.val and q.val are larger than root.val.
            root = root.right
        else:
            # the paths split (or you hit one of the nodes)
            # If the paths split then the current node is the LCA
            # The same is true if you hit one of the nodes
            return root
        
        return self.lowestCommonAncestor(root, p, q)
