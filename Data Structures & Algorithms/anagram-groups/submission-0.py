class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for i, n in enumerate(strs):
            sorted_word = "".join(sorted(n))
            anagrams.setdefault(sorted_word, []).append(n)

        return list(anagrams.values())

