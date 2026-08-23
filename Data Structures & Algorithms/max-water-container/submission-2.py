class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # The container is as tall as the smallest bar because otherwise the water spills out
        # So if we have a small bar, no matter what our other bar is, the height of the container is always as tall as the smaller bar
        # height = min(left_bar, right_bar), width = index of right bar - index of left bar
        # We want to return maximum height * width

        # We can use a 2 pointer approach and keep moving the pointers closer to each other by moving the smaller bar closer
        # This will work since the smallest bar is the height and we want to increase it
        # Let's walk through this example: height = [1,7,2,5,4,7,3,6], here we start with 1 and 6 on the edges, the height is 1 and width is 7, for a height of 1 (left bar) we have the biggest width, so this is the best area we will get with a bar with height 1, so let's look for a bigger left bar since it is the smaller one
        # We follow this approach until l = r

        max_area = 0
        l, r = 0, len(heights) - 1
        while l < r:
            width = r - l
            height = min(heights[r], heights[l])
            max_area = max(width * height, max_area)
            if heights[l] < heights[r]:
                l += 1
            else: 
                r -= 1
        return max_area

