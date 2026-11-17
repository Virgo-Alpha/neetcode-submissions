class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nlargest method returns a list and we pick the last num
        return heapq.nlargest(k, nums)[-1]
