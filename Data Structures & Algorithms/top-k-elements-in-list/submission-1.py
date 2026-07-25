from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # My implementation (fixed by ai)
        num_count = defaultdict(int)

        for num in nums:
            num_count[num] += 1

        # Sort items by frequency (value) descending
        sorted_count = sorted(num_count.items(), reverse=True, key=lambda x: x[1])

        # Extract the top k elements (just keys)
        return [item[0] for item in sorted_count[:k]]
