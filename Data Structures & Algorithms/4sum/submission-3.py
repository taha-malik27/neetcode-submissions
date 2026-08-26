class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quadruplets = set()
        nums.sort()

        for i in range(0, len(nums)):
            
            for j in range (i+1, len(nums)):
                left = j + 1
                right = len(nums) - 1
                
                while left < right:
                    # var for comparison
                    summation = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if summation == target:
                        # add too quadruplets
                        quadruplets.add(( nums[i], nums[j], nums[left], nums[right] ))
                        # update pointers
                        left += 1
                        right -= 1
                    
                    # if too little, increase sum
                    if summation < target:
                        left += 1
                    # if too much, decrease sum
                    if summation > target:
                        right -=1

        return list(quadruplets)





# -1 0 1 2 3 4