class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # bin search using 2 pointers

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if nums[m] <= nums[r]:
                # right hand side is sorted and target is not in it
                # the values in the right half range from nums[m] to nums[r].
                if nums[m] < target <= nums[r]:
                    # search the right half coz the target is there
                    l = m + 1
                else:
                    # search the left half
                    r = m - 1
                
            else: # left part is sorted because at least 1 half is sorted
                if nums[l] <= target < nums[m]:
                    # search the left half coz the target is there
                    r = m - 1
                else:
                    # search the right half
                    l = m + 1
                    
        return -1
