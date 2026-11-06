class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # We can use backtracking to recursively traverse these paths and make decisions to choose an element at each step. 
        # We maintain a variable sum, which represents the sum of all the elements chosen in the current path. 
        # We stop this recursive path if sum == target, and add a copy of the chosen elements to the result.
        

        # We recursively traverse the array starting from index i. 
        # At each step, we select an element from i to the end of the array. 
        # We extend the recursive path with elements where sum <= target after including that element.
        # This creates multiple recursive paths, and we append the current list to the result whenever the base condition is met.

        res = []
        
        def backtrack(index, current_combination, current_sum):
            # 1. Base cases (Success: sum == target, Failure: sum > target)
            if current_sum > target: return
            if current_sum == target:
                res.append(current_combination.copy())
                return

            # 2. Loop through choices starting from 'index'
            for i in range(index, len(nums)):
                # 3. Add to combination, recurse, then pop to backtrack
                current_combination.append(nums[i])

                backtrack(i, current_combination, current_sum + nums[i])

                current_combination.pop()
            
        # Start the recursion
        backtrack(0, [], 0)
        return res

            