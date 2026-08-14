import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = [1 for i in range(0, len(nums))]
        # make prefix of array where its 
        for i in range(0, len(nums)):
            if i == 0:
                prefix.append(1)
                continue
            prefix.append(nums[i-1]*prefix[i-1])
        

        for i in range(len(nums)-1,-1, -1):
            if i == len(nums) - 1:
                continue
            suffix[i] = nums[i+1] * suffix[i+1]

        products = []

        for i in range(0, len(nums)):
            products.append(suffix[i]*prefix[i])
        return products
            
        