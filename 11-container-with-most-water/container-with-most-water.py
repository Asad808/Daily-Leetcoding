class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) -1
        initial_area = 0
        while l < r:
            length = min(height[l], height[r])
            width = r - l
            area = length * width
            if area > initial_area:
                initial_area = area
            if height[l] < height[r]:
                l += 1
            elif height[l] >= height[r]:
                r -= 1
        return initial_area