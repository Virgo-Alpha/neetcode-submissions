class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            # For every number in the array, we take all the subsets we have so far and
            # create new subsets by adding the current number to each of them.
            res += [subset + [num] for subset in res]

        return res