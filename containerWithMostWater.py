class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        left = 0
        right = len(height)-1

        while left<right:
            area = min(height[left], height[right]) * (right-left)
            result = max(result, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return result