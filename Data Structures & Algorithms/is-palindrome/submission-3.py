class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.isAlphanumeric(s[l]):
                l += 1

            while l < r and not self.isAlphanumeric(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
        return True

    def isAlphanumeric(self, c):
        return (ord('a') <= ord(c) <= ord('z') or 
        ord('A') <= ord(c) <= ord('Z') or 
        ord('0') <= ord(c) <= ord('9'))


        # s = s.lower()
        # alphanumeric = ""

        # # ord['a'] - ord['z']
        # for t in s:
        #     alpha = ord(t) >= ord('a') and ord(t) <= ord('z')
        #     numeric = ord(t) >= ord('0') and ord(t) <= ord('9')
        #     if alpha or numeric:
        #         alphanumeric += t
        
        # return alphanumeric == alphanumeric[::-1]