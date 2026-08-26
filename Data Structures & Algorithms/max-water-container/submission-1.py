class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # set up 2 pointers
        left = 0
        right = len(heights) - 1
        largest_max = 0  #set up var to store largest area
        
        # set up vars to hold the highest left and right values seen so far.
        highest_left = 0
        highest_right = 0

        # 2 pointer loop
        while left < right:
            # first update the max heights for left and right so far
            if heights[left] > highest_left:
                highest_left = heights[left]

            if heights[right] > highest_right:
                highest_right = heights[right]
            
            # calculate area for this interation
            cur_max = (right - left) * min(heights[left], heights[right])

            # compare against global max seen so far and update if needed
            if cur_max> largest_max:
                largest_max = cur_max

            # move pointers based on a greedy approach. move the pointer with the smaller seen height
            if highest_left > highest_right:
                right-=1
            else:
                left+=1
        

        return largest_max
            