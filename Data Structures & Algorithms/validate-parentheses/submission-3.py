class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []

        brackets = {
            ')':'(',
            '}':'{', 
            ']': '['
        }

        b = 0

        # ? This only works if s had only brackets
        # ! If s had strings that were not brackets then this would fail
        for c in s:
            if c in brackets:
                if my_stack and my_stack[-1] == brackets[c]:
                    my_stack.pop()
                else:
                    return False
            else:
                my_stack.append(c)

        # Return True only if all opening brackets were successfully matched and popped
        return len(my_stack) == 0
