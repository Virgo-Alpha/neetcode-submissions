import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # bisect_left finds the lowest index where target can be inserted to maintain sorted order
        index = bisect.bisect_left(nums, target)
        return index if index < len(nums) and nums[index] == target else -1