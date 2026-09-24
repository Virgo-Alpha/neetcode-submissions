class Solution:
    def isValid(self, s: str) -> bool:
        # loop through the str
        # add opening brackets to the stack
        # Pop them when you encounter a similar closing bracket
        # Perhaps it would be better to use a hashmap
        # A stack is just a deque or a list with append and pop

        my_stack = []

        opening_brackets = set([
            '(', '[','{'
        ])

        brackets = {
            ')':'(',
            '}':'{', 
            ']': '['
        }

        b = 0

        while b < len(s):
            bracket = s[b]
            if bracket in opening_brackets:
                my_stack.append(bracket)
            elif bracket in brackets:
                # If stack is empty/top of stack doesn't match the required opening bracket
                if not my_stack or my_stack.pop() != brackets[bracket]:
                    return False


            b += 1

        # Return True only if all opening brackets were successfully matched and popped
        return len(my_stack) == 0
