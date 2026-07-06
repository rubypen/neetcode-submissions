class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, n in enumerate(nums):
            comp = target - n
            if comp in indices:
                return [indices[comp], i]
            indices[n] = i
        return [-1,-1]