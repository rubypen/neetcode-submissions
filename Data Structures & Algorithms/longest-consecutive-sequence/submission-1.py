class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        length = 0

        for n in nums:
            if (n - 1) not in nums:
                l = 0
                while (n + l) in nums:
                    l += 1
                length = max(length, l)
        
        return length