from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # Initialize variables
        freq_map = defaultdict(int)
        n = len(s)
        l = 0
        r = 0
        max_substring = 0
        # Set first count of letter up
        freq_map[s[r]] = 1
        # loop until r at end of string
        while r < n:
            # get window size and max freq in that window
            window_size = r - l + 1
            most_freq = max(freq_map.values())
            
            # key condition check: is this substring valid
            if window_size - most_freq <= k:
                # if valid, update max and increment right (expanding substring)
                max_substring = max(max_substring, window_size)
                r += 1
                # quick check to prevent out of range error on r at end of loop
                if r < n :
                    freq_map[s[r]] += 1
            else:
                # if invalid, increment left and decrement counter (shrinking substring)
                freq_map[s[l]] -= 1
                l += 1

        return max_substring

        
                    
            

