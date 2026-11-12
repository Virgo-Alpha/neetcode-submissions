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
        temp = []

        def dfs(i):
            # Base: i >= len(s)
            if i >= len(s):
                res.append(temp.copy())
                return

            # iterate
            for j in range(i, len(s)):
                sub = s[i:j+1]

                # both cases handled by 1 conditional, i.e.,
                # if palindrome append current substring and continue the loop
                # if not palindrome, continue the loop because we popped the substring
                if sub == sub[::-1]:
                    temp.append(sub)
                    dfs(j + 1)
                    temp.pop()

        dfs(0)

        return res