class Solution:
    def findMin(self, nums: List[int]) -> int:
        # nums was rotated between 1 and n times
        # rotating n times moves n items to the front
        # n % len(nums) is the remainder which is the number of items at the front
        # However, we do not know the value of n

        # Bruteforce would be to loop through, updating the min at each iteration
        # We should use 2 pointers, bin search and 1 loop, halving at each iteration
        # However, we need it sorted for bin search to work

        # The arr is rotated after sorting creating 2 segments
        # min(nums) is the first of either of these 2 segments
        # ? At least two of l, mid, and r will always be in the same sorted segment. 
        # Can you find conditions to eliminate one half and continue the binary search? 
        # Perhaps analyzing all possible conditions for l, mid, and r would help.
        # if left part has the min then nums[l] < nums[mid], else:
        # if right part has the min then nums[mid] < nums[r]

        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] < nums[r]:
                # This means that the right side is sorted
                # min can be the mid value or to the left
                # We can then discard the right
                r = mid
            else:
                l = mid + 1

        return nums[l]