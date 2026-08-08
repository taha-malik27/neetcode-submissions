class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
    
        for i in range(0, len(nums)):
            val = target - nums[i]
            
            # check if it does not exist in dictionary, if not, we add the current element i to dict so future elements can check against it
            if nums_dict.get(val) == None: 
                nums_dict[nums[i]] = i

            # if it does exist we return since thats the match
            else:
                # we switch order from i, j to j, i because i is always later in the array since the dict always contains elements that came before, so if we find it, its index always is before i.
                return [nums_dict.get(val), i]
            
# dupes work because since it overrides a previous value, and since exactly one pair exists, a value that was updated would never be returned since it would imply another pair and index exists.
# if the dupes are the answer like [5,5] with target 10, then the code returns before any overwrite would happen.