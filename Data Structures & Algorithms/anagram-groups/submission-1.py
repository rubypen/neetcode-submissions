class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # I ate with this hashmap implementation
        # anagrams = defaultdict(list)

        # for i, n in enumerate(strs):
        #     sorted_word = "".join(sorted(n))
        #     anagrams[sorted_word].append(n)

        # return list(anagrams.values())

        # Another with a hashmap but better runtime
        anagrams = defaultdict(list)

        for word in strs:
            count = 26 * [0]

            for char in word:
                count[ord(char) - ord('a')] += 1
            anagrams[tuple(count)].append(word)
        
        return list(anagrams.values())

