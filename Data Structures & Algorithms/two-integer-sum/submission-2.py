class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
    
        for i in range(0, len(nums)):
            val = target - nums[i]
            if nums_dict.get(val) == None:
                nums_dict[nums[i]] = i
            else:
                return [nums_dict.get(val), i]
            

