class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # We need to sort first then skip identical elements
        candidates.sort()
        res = []  # perhaps this should be a set then?

        def backtrack(i, curr_sum, curr_combination):
            """
            We can use the index of the candidates to loop through,
            storing the current sum and current_combinations
            """

            # Invalid case
            if curr_sum > target: return

            # Base case where we append a copy; when curr_sum equals sum
            if curr_sum == target:
                res.append(curr_combination.copy())
                return

            # we loop through and add
            for idx in range(i, len(candidates)):
                # we need to skip duplicates so:
                if candidates[idx] == candidates[idx - 1] and idx > i:
                    continue

                curr_combination.append(candidates[idx])
                backtrack(idx + 1, curr_sum + candidates[idx], curr_combination)

                curr_combination.pop()

        
        backtrack(0, 0, [])

        return res