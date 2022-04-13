class Solution:
    def maxArea(self, height: List[int]) -> int:
        results = 0
        left, right = 0, len(height) - 1
        for i in range(len(height) - 1, 0, -1):
            if height[left] < height[right]:
                results = max(results, height[left] * i)
                left = left + 1
            else:
                results = max(results, height[right] * i)
                right = right - 1
        return results