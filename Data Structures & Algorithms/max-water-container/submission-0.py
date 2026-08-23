class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0


        for l in range(len(heights)):
            for r in range(l + 1, len(heights)):
                width = r - l
                height = min(heights[l], heights[r])
                max_water = max(width * height, max_water)

        return max_water
