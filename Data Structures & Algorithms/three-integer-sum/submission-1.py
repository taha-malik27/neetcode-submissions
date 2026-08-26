class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort() #O(n log n)

        # loop through i index
        for i in range(0, len(nums)):
            # for each i, we set 2 pointers infront, left and right
            left = i + 1
            right = len(nums) - 1
            # sorted, so checking adjacent values avoids duplicates (skippiing first index)
            if nums[i] == nums[i-1]  and i > 0: 
                continue

            # nested loop which created time complexity of n^2 /2 but strictly just O(n^2)
            while left < right:
                # var for comparison
                summation = nums[i] + nums[left] + nums[right]
                # check if i,left,right add to 0
                if summation == 0:
                    # add too triplets
                    triplets.append([ nums[i], nums[left], nums[right] ])
                    # update pointers
                    left += 1
                    right -= 1
                    # sorted, so checking adjacent values avoids duplicates just like index i
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                # if too little, increase sum
                if summation < 0:
                    left += 1
                # if too much, decrease sum
                if summation > 0:
                    right -=1

        return triplets

