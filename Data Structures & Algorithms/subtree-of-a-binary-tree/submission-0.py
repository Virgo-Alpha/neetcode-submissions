# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # We recurse root's nodes until we find a node matching subroot's root node
        # Then we recursively determine if all the values of that match

        if not subRoot: return True

        if not root: return False
        
        def sameTree(root1, root2):
            """This is a dfs traversal"""
            if not root1 and not root2: return True

            if root1 and root2 and root1.val == root2.val:
                # This is the same tree so recurse over its children
                return (sameTree(root1.left, root2.left) and sameTree(root1.right, root2.right))
            return False

        if sameTree(root, subRoot):
            # This is when when the root of both trees match
            return True
        
        # Else we search both left and right recursively and return whichever is Truthy
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
