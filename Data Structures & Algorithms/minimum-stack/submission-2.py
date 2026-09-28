class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        max_value = float('inf')

        if self.stack:
            for val in self.stack:
                if val < max_value:
                    max_value = val

        return max_value
