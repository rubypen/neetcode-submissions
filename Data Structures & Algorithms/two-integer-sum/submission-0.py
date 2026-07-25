class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in num_dict:
                return [num_dict[needed], i]
            else: 
                num_dict[nums[i]] = i 
        
        return [0, 0]