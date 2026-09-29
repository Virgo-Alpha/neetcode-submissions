class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # target for both complexities is O(n) so one loop through
        stack = []

        for token in tokens:
            # check if operator or operand
            # if operand, push to the stack
            
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                # Right operand is popped first
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                # Right operand is popped first
                num2 = stack.pop()
                num1 = stack.pop()
                # int() division truncates towards zero, satisfying LeetCode constraints
                stack.append(int(num1 / num2))
            else:
                # If it's not an operator, it's a number
                stack.append(int(token))

        return stack.pop()