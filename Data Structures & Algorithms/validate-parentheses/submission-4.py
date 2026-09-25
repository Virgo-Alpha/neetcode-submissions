class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []

        brackets = {
            ')':'(',
            '}':'{', 
            ']': '['
        }

        # Create a set of valid opening brackets for quick lookup
        opening_brackets = set(brackets.values())

        b = 0

        for c in s:
            if c in brackets:
                if my_stack and my_stack[-1] == brackets[c]:
                    my_stack.pop()
                else:
                    return False
            elif c in opening_brackets:
                my_stack.append(c)

        # Return True only if all opening brackets were successfully matched and popped
        return len(my_stack) == 0
