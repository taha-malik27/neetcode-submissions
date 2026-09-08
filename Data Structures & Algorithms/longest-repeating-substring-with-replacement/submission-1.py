from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = defaultdict(int)
        n = len(s)
        l = 0
        r = 0
        max_substring = 0
        freq_map[s[r]] = 1
        while r < n:
            
            window_size = r - l + 1
            most_freq = max(freq_map.values())
            if window_size - most_freq <= k:
                max_substring = max(max_substring, window_size)
                r += 1
                if r < n :
                    freq_map[s[r]] += 1
            else:
                freq_map[s[l]] -= 1
                l += 1

        return max_substring

        
                    
            

