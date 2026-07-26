class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alphanumeric = ""

        # ord['a'] - ord['z']
        for t in s:
            alpha = ord(t) >= ord('a') and ord(t) <= ord('z')
            numeric = ord(t) >= ord('0') and ord(t) <= ord('9')
            if alpha or numeric:
                alphanumeric += t
        
        return alphanumeric == alphanumeric[::-1]