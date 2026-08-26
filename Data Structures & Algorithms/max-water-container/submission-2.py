class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # set up 2 pointers
        left = 0
        right = len(heights) - 1
        largest_max = 0  #set up var to store largest area

        # 2 pointer loop
        while left < right:
            
            # calculate area for this interation
            cur_max = (right - left) * min(heights[left], heights[right])

            # compare against global max seen so far and update if needed
            if cur_max> largest_max:
                largest_max = cur_max

            # move pointers based on a greedy approach. move the pointer with the smaller height
            if heights[left] > heights[right]:
                right-=1
            else:
                left+=1
        
        return largest_max
            