class Solution:
    # ---- No guarantee of space 
    # def isAnagram(self, s: str, t: str) -> bool:
    #     letter_ct = {}

    #     if len(t) != len(s):
    #         return False

    #     return sorted(s) == sorted(t)

    # ---- Hashmaps
    # def isAnagram(self, s: str, t: str) -> bool:
    #     count_s, count_t = {}, {}

    #     if len(s) != len(t):
    #         return False

    #     for i in range(len(s)):
    #         count_s[s[i]] = 1 + count_s.get(s[i], 0)
    #         count_t[t[i]] = 1 + count_t.get(t[i], 0)
        
    #     return count_s == count_t

    # ---- Clever with array
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 

        count = 26 * [0]
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        
        return True

        