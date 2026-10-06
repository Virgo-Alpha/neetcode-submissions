class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # You can use 2 pointers which was the 1st algorithm
        # Here, use recursion and employ a helper function
        l, r = 0, len(nums) - 1

        def helper(l, r):
            if l > r:
                return -1
                
            middle = (l + r) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                r = middle - 1
                return helper(l, r)
            elif nums[middle] < target:
                l = middle + 1
                return helper(l, r)

        return helper(l, r)
