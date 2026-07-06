from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for key, v in count.items():
            buckets[v].append(key)
        
        res = []

        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        return []


        