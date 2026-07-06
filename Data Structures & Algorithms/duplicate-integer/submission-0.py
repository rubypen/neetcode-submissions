from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = defaultdict(int)

        for n in nums: 
            numbers[n] += 1
            if numbers[n] > 1:
                return True
        return False
        
