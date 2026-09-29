class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Using recursion:
        #  - Each number is a base case
        #  - Each operator is a recursive call
        #  - final return value is the fully evaluated expression

        # The Algorithm:
        # 1. Start from the end of the token list
        # 2. Recursively:
        # - Pop a token.
        # - If it is a number, return it.
        # - If it is an operator:
        #   - Recursively compute the right operand.
        #   - Recursively compute the left operand.
        #   - Apply the operator to both results.
        #   - Return the computed value.
        # 3. The first completed call returns the final answer.

        def recursiveRPN_eval():
            token = tokens.pop()

            if token not in set(["+", "-", "*", "/"]):
                return int(token)

            right, left = recursiveRPN_eval(), recursiveRPN_eval()

            if token == '+':
                return left + right
            elif token == '-':
                return left - right
            elif token == '*':
                return left * right
            elif token == '/':
                return int(left / right)

        return recursiveRPN_eval()
        