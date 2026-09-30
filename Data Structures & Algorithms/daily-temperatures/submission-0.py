class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # We can only loop once since ideal time complexity is O(n)
        result = [0] * len(temperatures)
        
        # A stack keeps track of days that are still waiting for a warmer temperature.
        stack = [] # pair: [temp, idx]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                # This is the next warmer day: we pop it, compute the diff and continue
                # We pop it because we have found its next warmer day
                # While loop runs until all elements less than current temp are popped
                stackT, stackInd = stack.pop()
                result[stackInd] = i - stackInd
            # If not greater than any in the stack, we add to the stack
            stack.append((t, i))

        return result
