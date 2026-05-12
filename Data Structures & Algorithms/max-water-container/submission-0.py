class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if(len(heights) < 2): return 0
        max_water = 0
        left = 0
        right = len(heights)-1
        while left < right:
            lh = heights[left]
            rh = heights[right]
            max_height = min(lh, rh)
            hold_water = (right-left)*max_height
            max_water = max(hold_water, max_water)
            if(lh < rh): left += 1
            else: right -= 1
        return max_water
