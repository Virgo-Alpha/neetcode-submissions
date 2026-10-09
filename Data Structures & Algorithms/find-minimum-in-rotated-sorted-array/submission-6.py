class Solution:
    def findMin(self, nums: List[int]) -> int:
        # in nums: one part is always sorted, and the other part contains the rotation (and the minimum element).
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                # If the left half is sorted, then the minimum cannot be there, so we search the right half.
                l = m + 1
            else:
                # If the right half is sorted, then the minimum must be in the left half (or at the midpoint).
                r = m - 1
        return res