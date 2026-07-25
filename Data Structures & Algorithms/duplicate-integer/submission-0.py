class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        for num in nums:
            if my_dict.get(num, 0) + 1 > 1:
                return True
            else:
                my_dict[num] = 1
        return False
        
