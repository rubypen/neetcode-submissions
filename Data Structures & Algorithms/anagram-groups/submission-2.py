from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # [0] * 26 ; ord['z'] - ord[letter]
        anagrams = defaultdict(list)

        for s in strs:
            counts = [0] * 26
            # count occurence of each letter within current word
            for l in s:
                idx = ord('z') - ord(l)
                counts[idx] += 1
            # add anagram to dictionary
            anagrams[tuple(counts)].append(s)
        
        return list(anagrams.values())