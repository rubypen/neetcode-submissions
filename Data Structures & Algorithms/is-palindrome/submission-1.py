class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower()
        
        def filterAlnum(x):
            return ord(x) >= ord('a') and ord(x) <= ord('z') or ord(x) >= ord('0') and ord(x) <= ord('9')
        filteredStr = "".join(filter(filterAlnum, string))

        reversedStr = filteredStr[::-1]

        return reversedStr == filteredStr