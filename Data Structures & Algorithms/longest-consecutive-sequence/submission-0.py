from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums) #use set as we dont care about dupes and O(1) lookups for a number in nums 
        starters = set()
        
        # first find all the numbers that indicate a start of a sequence, which is if it has no consecutive number before it.
        for num in numsSet:
            if num - 1 not in numsSet:
                starters.add(num)
        
        # now go through all sequences via starters keeping track of the max sequence so far
        max_sequence = 0
        for starter in starters:
            cur_num = starter
            cur_sequence = 1
            # still O(n) time despite loop in loop, for each starter we loop through their sequences once, and with no dupes, 
            # its just all unique numbers in nums looked up only once
            while cur_num + 1 in numsSet:
                cur_sequence += 1
                cur_num += 1
            
            # update max sequence if the current sequence count is the new best
            if cur_sequence >= max_sequence:
                max_sequence = cur_sequence

        return max_sequence

