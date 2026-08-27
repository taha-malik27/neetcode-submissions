class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0 # init max_area variable to min value
        # set up 2 pointers
        left = 0
        right = len(heights) - 1
        # set up pointer loop
        while left < right:
            # get area
            area = (right - left)*min(heights[left], heights[right])
            # update max_area
            if area > max_area:
                max_area = area
            # greedy approach to iterating, choose the smaller height pointer and move it along 
            # (aim is to find a potentially higher height than before)
            if heights[left] > heights[right]:
                right-=1
            else:
                left+=1
        return max_area