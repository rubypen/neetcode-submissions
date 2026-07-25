class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0

        # set_nums = sorted(set(nums))

        # counts = [1]
        # for i in range(1, len(set_nums)):
        #     if set_nums[i] == set_nums[i - 1] + 1:
        #         counts[-1] += 1
        #     else:
        #         counts.append(1)

        # return max(counts)

        # YT 
        numSet = set(nums)
        longest = 0

        for n in numSet:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
