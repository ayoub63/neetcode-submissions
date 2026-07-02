class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        value = 0

        while r > l:
            area = (r - l) * min(heights[l], heights[r])
            value = max(value, area)
            if heights[l] > heights[r]:
                r -= 1

            else:
                l+= 1

        return value
         