class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l != r:
            sumN = numbers[l] + numbers[r]
            if sumN == target:
                return [l + 1, r + 1]
            elif sumN > target:
                r -= 1
            else:
                l += 1

        return []
