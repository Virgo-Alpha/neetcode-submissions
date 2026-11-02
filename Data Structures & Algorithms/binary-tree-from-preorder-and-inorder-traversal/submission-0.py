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

        # After getting the root node from pre-order traversal, we then look for the index of that node in the in-order array.
        # We can use a hash map to get the index of any node in the in-order array in O(1) time.

        # We use Depth First Search (DFS) to construct the tree. 
        # A global variable tracks the current index in the pre-order array. 
        # Indices l and r represent the segment in the in-order array for the current subtree. 
        # For each node in the pre-order array, we create a node, find its index in the in-order array using the hash map, and recursively build the left and right subtrees by splitting the range [l, r] into two parts for the left and right subtrees.

        idx = 0
        
        # Map each value in inorder to its index
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        def dfs(l, r):
            nonlocal idx

            # Base case: if the range is invalid, there are no nodes to create
            if l > r: return None
                
            # Pick the current element from preorder as the root
            root_val = preorder[idx]
            root = TreeNode(root_val)
            idx += 1
            
            # Find where this root splits the inorder array
            mid = inorder_map[root_val]
            
            # Crucial: Build the left subtree first because preorder goes Root -> Left -> Right
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            
            return root
            
        # Kick off the recursion with the full range of the inorder array
        return dfs(0, len(inorder) - 1)


