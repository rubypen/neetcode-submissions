class Solution:
    def isValid(self, s: str) -> bool:
        parens = { "]" : "[", ")" : "(", "}" : "{"}
        stk = []
        for p in s:
            if stk and p in parens:
                if stk[-1] == parens[p]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(p)
            
        return True if not stk else False