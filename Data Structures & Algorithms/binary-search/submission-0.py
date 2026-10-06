class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Hint 1: Instead of cutting the list into smaller pieces (which resets the indices), keep the original list entirely intact and use two pointer variables to track your boundaries:
        # Hint 2: To stop the recursion safely, you need to recognize when your search area has completely collapsed and the target definitely isn't there
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        # use 2 pointers
        l, r = 0, len(nums) - 1

        while l <= r:
            middle = (r + l) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                # The target is on the left so we move the right pointer
                r = middle - 1
            elif nums[middle] < target:
                # The target is on the right so we move the left pointer
                l = middle + 1
            
        return -1
