class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return
        
        nums.sort()
        
        i = 0

        final_set = set()

        for i in range(len(nums)):
            target = -nums[i]
            j = i + 1
            
            k = len(nums) - 1
            
            while j < k:
                current_sum = nums[j] + nums[k]
                if current_sum == target:
                    final_set.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                if current_sum < target:
                    j += 1
                if current_sum > target:
                    k -= 1
            i += 1

        return [list(triplet) for triplet in final_set]
