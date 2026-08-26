class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        largest_max = 0
        highest_left = 0
        highest_right = 0
        while left < right:
            if heights[left] > highest_left:
                highest_left = heights[left]

            if heights[right] > highest_right:
                highest_right = heights[right]
            
            cur_max = (right - left) * min(heights[left], heights[right])


            if cur_max> largest_max:
                largest_max = cur_max
                
            if highest_left > highest_right:
                right-=1
            else:
                left+=1
        

        return largest_max
            