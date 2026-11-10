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
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res
