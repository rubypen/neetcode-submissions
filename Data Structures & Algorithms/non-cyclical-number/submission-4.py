class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSq(n):
            tot = 0
            while n != 0:
                digit = n % 10
                tot += digit * digit
                n = n // 10
            return tot

        output = n
        seen = set()
        while output != 1:
            output = sumOfSq(output)
            if output in seen:
                return False
                
            seen.add(output)
            n = output
        return True


