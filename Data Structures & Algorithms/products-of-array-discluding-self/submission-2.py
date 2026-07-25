class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # populate prefix -> set prefix in i, update prefix
        # populate postfix -> multiply i by postfix, update postfix
        # 0, 1, 2, 3
        # output =[1 * 6 = 6,0 * 6 = 0,0 * 3 = 0 ,0 * 1 = 0]
        # = [6,0,0,0]
        # prefix = 1 -> 0*0 = 0 -> 0 * 1 = 0 -> 0 * 2 = 0
        # postfix = 1 -> 1 * 3 = 3 -> 3 * 2 = 6, 6 * 1 = 6 -> 6 * 0 = 0
        output = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        
        return output

        # Space: O(len(nums))
        # Time: O(2n) = O(n)



