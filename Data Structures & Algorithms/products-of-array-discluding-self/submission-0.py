class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # First Implementation:
        # output = [1] * len(nums)

        # for idx_exclude in range(len(nums)):
        #     for i in range(len(nums)):
        #         output[idx_exclude] *= nums[i] if i != idx_exclude else 1
        
        # return output

        # Second Implementation:
        # Game Plan: with division; count zeros and find product
        # if there are more than 1 zeros, return a list of zeros
        # otherwise find the correct product
        #
        # prod = 1
        # zero_ct = 0

        # for num in nums:
        #     if num == 0:
        #         zero_ct += 1
        #     prod *= num if num != 0 else 1
        
        # if zero_ct > 1:
        #     return [0] * len(nums)
        # elif zero_ct == 0:
        #     output = list(map(lambda x: prod//x, nums))
        # else:
        #     output = [0 if num != 0 else prod for num in nums]
        
        # return output

        # Third Implementation
        # Game Plan: Keep an account of prefixes and postfixes to update res
        res = [1] * len(nums)
        nums_len = len(nums)

        prefix = 1
        for i, num in enumerate(nums):
            res[i] *= prefix
            prefix *= num
        postfix = 1
        for i in range(nums_len - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res

        
        


        