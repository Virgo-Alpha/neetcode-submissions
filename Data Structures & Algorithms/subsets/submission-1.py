class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        The idea is to build all possible subsets by making a choice at each step:
        for every number, we have two options — include it or exclude it.
        This naturally forms a decision tree.

        --> Backtracking helps us explore both choices:

        Add the current number → explore further
        Remove it (undo) → explore without it
        Whenever we reach the end of the array, the current list represents one
        complete subset, so we store it.

        This systematically generates all 2ⁿ subsets.
        """
        res = []  # final list of all subsets
        subset = []  # current subset being built

        def dfs(i):
            if i >= len(nums):
                # Base case: If i equals the len of the input, add a copy of subset to res and return
                res.append(subset.copy())
                return
            # Choice 1: include nums[i], recurse to the next idx to explore deeper
            subset.append(nums[i])
            dfs(i + 1)

            # Backtrack: Remove nums[i] to reset the state for the next branch
            subset.pop()

            # Choice 2: Exclude nums[i] and explore deeper
            dfs(i + 1)

        dfs(0)
        return res