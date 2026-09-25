class Solution:
    def isValid(self, s: str) -> bool:
        # loop through the str
        # add opening brackets to the stack
        # Pop them when you encounter a similar closing c
        # Perhaps it would be better to use a hashmap
        # A stack is just a deque or a list with append and pop

        my_stack = []

        # ! Remove the set and only use the hashmap
        # opening_brackets = set([
        #     '(', '[','{'
        # ])

        brackets = {
            ')':'(',
            '}':'{', 
            ']': '['
        }

        b = 0

        # ? Make this more pythonic
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
