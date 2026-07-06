class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(n)
        if len(s) != len(t):
            return False

        count = defaultdict(int)

        for i in range(len(s)):
            sl = s[i]
            tl = t[i]

            count[sl] += 1
            count[tl] -= 1

        return all(v == 0 for v in count.values())

        # # O(nlogn)
        # s = sorted(s)
        # t = sorted(t)

        # return s == t