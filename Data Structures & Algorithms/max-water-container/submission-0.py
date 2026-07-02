class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_value = 0

        for i in range(0, len(heights)):
            for j in range(len(heights) - 1, i, -1):
                curr = min(heights[i], heights[j]) * (j - i)
                if curr > max_value:
                   max_value = curr

        return max_value 