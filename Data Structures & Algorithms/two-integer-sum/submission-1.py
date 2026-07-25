class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for i, n in enumerate(nums):
            diff = target - nums[i]
            if diff in num_dict:
                return [num_dict[diff], i]
            num_dict[n] = i
        return [0, 0]