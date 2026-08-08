class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = {} # counter that tracks duplicates
        for num in nums:
            if counter.get(num) == None: #if the counter does not have it then simply
                counter[num] = 1
            else:
                counter[num] += 1  # add to counter if already exists
        # do another sequential for loop to check if any counter is >1, maintains o(n) complexity
        for value in counter.values():
            if value > 1:
                return True
        return False


        