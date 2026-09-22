class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0

        l, r = 0, len(heights) - 1

        while l < r:
            if heights[l] < heights[r]:
                area = max(area, heights[l] * (r - l))
                l += 1
            
            else:
                area = max(area, heights[r] * (r - l))
                r -= 1
        
        return area
