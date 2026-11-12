class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # We can use backtracking to recursively traverse the string with indices j 
        # (start of the current substring) and i (current iterating index). 
        # At each step, we either skip partitioning at the current index or, 
        # if the substring from j to i is a palindrome, make a partition, 
        # update j = i + 1, and start a new substring. 
        # The base condition to stop the recursion is when j reaches the end of the string.

        # We start with j = 0, i = 0 and a temporary list which stores the substrings 
        # from the partitions. 
        # Then we recursively iterate the string with the index i. 
        # At each step we apply the 2 decisions accordingly. 
        # At the base condition of the recursive path, 
        # we make a copy of the current partition list and add it to the result.
        res = []

        def backtrack(j, i, temp):
            # Base: j == len(s)
            if j == len(s):
                res.append(temp.copy())
                return

            # Base case 2
            if i == len(s): return

            # Choice 1: Skip partitioning at index i (extend current substring to i + 1)
            backtrack(j, i + 1, temp)

            # Choice 2: Partition at index i if the substring s[j : i+1] is a palindrome
            sub = s[j : i + 1]
            if sub == sub[::-1]:
                temp.append(sub)
                backtrack(i + 1, i + 1, temp)  # Update both j and i to i + 1
                temp.pop()                     # Undo the append for other branches

        backtrack(0, 0, [])
        
        return res