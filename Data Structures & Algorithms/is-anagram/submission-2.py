from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # racecar, carrace 
        count = defaultdict(int)
        for l in s:
            count[l] += 1
        
        for l in t:
            count[l] -= 1

        for c in count.values():
            if c > 0 or c < 0:
                return False
        return True