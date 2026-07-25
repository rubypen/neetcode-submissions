class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_ct = {}

        if len(t) != len(s):
            return False

        return sorted(s) == sorted(t)

        