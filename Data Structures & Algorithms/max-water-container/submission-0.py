class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxi = 0
        l, r = 0, len(heights) - 1

        while l < r:
            left, right = heights[l], heights[r]
            total = min(left, right) * (r - l)
            if total > maxi:
                maxi = total
            if left >= right:
                r -= 1
            else:
                l += 1

        return maxi