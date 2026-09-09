class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # init vars
        l, r = 0, len(nums) - 1
        t = target
        while l <= r:
            # check if target is left or right first (easy pickings)
            if t == nums[r]:
                return r
            if t == nums[l]:
                return l
            
            # calculate mid and check if its target
            m = (l+r) // 2
            if t == nums[m]:
                return m

            # key condition: move towards the side that can contain the target given where the rotation is and the ascending order
            if nums[m] < nums[r]:
                # left side has rotation
                if nums[m] < t < nums[r]:
                    # move to right (non rotation) side, as m<t<r and since asc order must be here if exists
                    l = m + 1
                else:
                    # move to left (rotation) side, since ! m<t<r, target cant be on the right side, asc ordering forbids it, so move left
                    r = m - 1
                    
            else:
                # right side has rotation
                if nums[l] < t < nums[m]:
                    # move to left (non rotation) side, as l<t<m and since asc order must be here if exists
                    r = m - 1
                else:
                    # move to right (rotation) side, since ! l<t<m, target cant be on the left side, asc ordering forbids it, so move right
                    l = m + 1
        
        # if BS doesnt return, nothing found, thus, remove
        return -1
