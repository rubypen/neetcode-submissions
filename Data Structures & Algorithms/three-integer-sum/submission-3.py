from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Game Plan: Sort the list to take care of this problem like we would
        # 2 sum 
        # Then iterate through the left values and perform two sum on what is left
        # Ensure no duplicates by checking if curr, and left are not equal to their
        # previous values
        nums.sort()
        ans = []

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1

            while l < r:
                total = num + nums[l] + nums[r]
                if total == 0:
                    ans.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                elif total > 0:
                    r -= 1
                else:
                    l += 1

        return ans        
        