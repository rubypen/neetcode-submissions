class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower()
        
        filteredStr = "".join(filter(str.isalnum, string))

        reversedStr = filteredStr[::-1]

        return reversedStr == filteredStr