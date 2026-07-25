class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Game Plan: two pointers; if smaller height, in/decrement pointer;
        # Compare area to prevMax and update when necessary; 
        if not heights:
            return 0
            
        maxArea = 0 
        l, r = 0, len(heights) - 1

        while l < r:
            left, right = heights[l], heights[r]
            currArea = min(left, right) * (r - l)
            if currArea > maxArea:
                maxArea = currArea
            if left >= right:
                r -= 1
            else:
                l += 1
        
        return maxArea
