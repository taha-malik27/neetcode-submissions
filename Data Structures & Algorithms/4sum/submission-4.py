class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quadruplets = list()
        nums.sort()

        for i in range(0, len(nums)):

            # prevent dupes for i index
            if nums[i] == nums[i-1]  and i > 0: 
                continue

            for j in range (i+1, len(nums)):
                left = j + 1
                right = len(nums) - 1
                
                # prevent dupes for j index
                if nums[j] == nums[j-1] and j > i + 1 : 
                    continue
                
                while left < right:
                    # var for comparison
                    summation = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if summation == target:
                        # add too quadruplets
                        quadruplets.append([ nums[i], nums[j], nums[left], nums[right] ])
                        # update pointers
                        left += 1
                        right -= 1
                        # sorted, so checking adjacent values avoids duplicates just like index i j
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    # if too little, increase sum
                    if summation < target:
                        left += 1
                    # if too much, decrease sum
                    if summation > target:
                        right -=1

        return quadruplets





# -1 0 1 2 3 4