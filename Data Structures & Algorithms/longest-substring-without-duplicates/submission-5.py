class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # set to track unique chars of current substring
        tracker = set()
        # initialize substring trackers
        longest_substring = ""
        current_substring = ""
        # initialize vars
        l = 0; r = 0; n = len(s)

        while r <= n-1:
            # logic for if repeated char appears (reset)
            if s[r] in tracker:
                # move left until no dupe left
                while s[l] != s[r]:
                    # remove characters lost due to removing dupe
                    tracker.remove(s[l])
                    l+=1
                l+=1
                current_substring = s[l:r+1]
            

            # logic for if new char appears
            else:
                # update substrings
                current_substring = s[l:r+1]
                if len(longest_substring) < len(current_substring):
                    longest_substring = current_substring
                # update tracker
                tracker.add(s[r])
                # only move right forward when new char found
            r+=1
        
        return len(longest_substring)