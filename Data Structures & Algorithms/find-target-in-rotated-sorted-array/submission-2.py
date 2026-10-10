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
                if nums[m] < target  and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
                
            elif nums[l] <= nums[m]:
                if nums[l] <= target and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
                    
        return -1
