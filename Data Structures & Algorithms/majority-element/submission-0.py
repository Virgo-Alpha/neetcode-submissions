from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        n = len(nums)

        for k, v in count.items():
            if v > (n / 2):
                return k