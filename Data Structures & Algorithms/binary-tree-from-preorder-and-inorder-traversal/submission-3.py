# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder starts with root then left, then right
        # inorder starts with left, then root, then right


        inorder_idx = {val: i for i, val in enumerate(inorder)}
        pre_iter = iter(preorder)

        def helper(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            root_val = next(pre_iter)
            root = TreeNode(root_val)
            pos = inorder_idx[root_val]
            root.left = helper(left, pos - 1)
            root.right = helper(pos + 1, right)
            return root

        return helper(0, len(inorder) - 1)