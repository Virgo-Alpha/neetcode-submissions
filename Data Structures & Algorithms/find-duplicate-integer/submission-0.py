class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Use Floyd's cycle detection algorithm. 
        # Initialize a slow and a fast pointer at index 0. 
        # Repeatedly move the slow pointer one step with slow = nums[slow] and the fast pointer two steps with fast = nums[nums[fast]] until they meet. Is this first meeting point necessarily the duplicate?

        # The first meeting point may be anywhere inside the cycle. 
        # After the pointers meet, initialize a second slow pointer at index 0. 
        # Move both slow pointers one step at a time using the values in nums. 
        # The index where they meet is the cycle entry, which is the duplicate number.

        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

