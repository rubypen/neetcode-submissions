class Solution:
    def isHappy(self, n: int) -> bool:
        output = n
        seen = set()
        while output != 1:
            output = 0
            while n / 10 != 0:
                digit = n % 10
                output += digit * digit
                n = n // 10
            if output in seen:
                return False
            seen.add(output)
            n = output
        return True


