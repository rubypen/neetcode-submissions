class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        water = 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = [0, 0]

        while l < r:
            left, right = height[l], height[r]
            if left < right:
                l += 1
                leftMax = max(leftMax, left)
                water += leftMax - left
            else:
                r -= 1
                rightMax = max(rightMax, right)
                water += rightMax - right

        return water
