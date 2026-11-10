class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        When the count of closing brackets exceeds the count of opening brackets, 
            the string becomes invalid. 
        Therefore, we can maintain two variables, open and close, 
            to track the number of opening and closing brackets. 
        We avoid exploring paths where close > open. 
        Once the string length reaches 2n, we add it to the result.
        """
        if not n: return []

        res = []

        def backtrack(opening, close, curr_str):
            # invalid case
            if close > opening: return

            # Base case: valid string found
            if close == opening and len(curr_str) == 2 * n:
                res.append(curr_str)
                return

            # For parentheses, you don't need a loop; you just need to branch into your two choices
            # Choice 1: Add opening bracket if we haven't reached the limit
            if opening < n:
                backtrack(opening + 1, close, curr_str + "(")
            
            # Choice 2: Add closing bracket only if it won't exceed opening brackets
            if close < n:
                backtrack(opening, close + 1, curr_str + ")")
                

        backtrack(0, 0, "")

        return res
