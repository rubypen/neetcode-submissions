class Solution:
    def isValid(self, s: str) -> bool:
        # () {} []
        # cases: [, ], random pairing
        pairs = { ")" : "(", "]" : "[", "}" : "{", }
        opening = []

        for p in s:
            if p in pairs:
                if opening and pairs[p] == opening[-1]:
                    opening.pop()
                else:
                    return False
            else: 
                opening.append(p)

        return True if not opening else False
