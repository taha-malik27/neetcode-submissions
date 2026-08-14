class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = 1
        suffix = 1
        # make prefixes first directly in res
        for i in range(0, len(nums)):
            if i == 0:
                res.append(prefix)
                continue
            prefix *= nums[i-1]
            res.append(prefix)

        # make suffixes now while also doing multiplication step for result
        for i in range(len(nums)-1,-1, -1):
            if i == len(nums) - 1:
                res[i] *= suffix
                continue
            suffix *= nums[i+1]
            res[i] *= suffix

        return res
            
        