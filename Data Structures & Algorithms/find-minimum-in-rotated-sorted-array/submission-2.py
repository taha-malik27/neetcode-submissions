class Solution:
    def findMin(self, nums: List[int]) -> int:
        # set up vars
        l = 0
        r = len(nums)- 1
        minNum = 1001 # since constraint is 1000 set it to 1001

        while l <= r:
            # key condition: check ordering of l, r
            if nums[l] < nums[r]:
                # if in perfect order, select lowest value and return
                minNum = min(nums[l], minNum)
                break

            # mid point index
            m = (l + r) // 2

            # track lowest value seen so far
            minNum = min(nums[m], minNum)
            # key condition: check which side is ordered and which is split by rotation
            
            if nums[m] < nums[r]:
                # right side ordered, left side has rotation, min/max is always near rotation
                r = m - 1
            
            elif nums[l] <= nums[m]:
                # left side ordered, right side has rotation, min/max is always near rotation
                l = m + 1
                
        # return min 
        return minNum
