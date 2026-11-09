class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        We start by sorting the input array. 
        Then, we recursively iterate through the array from left to right, extending recursive paths
         by including or excluding each element. 
        To avoid duplicate subsets, we skip an element if it is the same as the previous one. 
        Finally, we return the generated subsets as a list.
        """
        res = []
        nums.sort()

        def backtrack(i, subset):
            # Base case: all subsets should be appended to res
            res.append(subset.copy())

            # loop and backtrack
            # the loop handles the invalid case of when idx exceeds len of nums
            for idx in range(i, len(nums)):
                # skip duplicates
                if idx > i and nums[idx] == nums[idx - 1]:
                    continue
                
                subset.append(nums[idx])

                backtrack(idx + 1, subset)

                subset.pop()

        backtrack(0, [])

        return res