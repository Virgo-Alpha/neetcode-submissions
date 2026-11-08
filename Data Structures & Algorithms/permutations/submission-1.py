class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # We need a means to track used elements
        res = []

        def backtrack(permutation, used):
            # invalid state
            if len(permutation) > len(nums): return

            # valid successful state
            if len(permutation) == len(nums):
                res.append(permutation.copy())
                return

            # loop, add element, backtrack, pop element
            for idx in range(len(nums)):
                if nums[idx] not in used:
                    permutation.append(nums[idx])
                    used.add(nums[idx])
                    backtrack(permutation, used)
                    permutation.pop()
                    used.remove(nums[idx])

        backtrack([], set())

        return res