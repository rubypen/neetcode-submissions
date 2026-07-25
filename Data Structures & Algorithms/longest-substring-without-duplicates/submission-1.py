class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        maxLen = 0
        l = 0
        seen = {}

        for idx, let  in enumerate(s):
            if let in seen:
                l = max(seen[let] + 1, l)
            seen[let] = idx
            maxLen = max(maxLen, idx - l + 1)
        
        return maxLen