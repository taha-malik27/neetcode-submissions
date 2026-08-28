class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # set to track unique chars of current substring
        tracker = set()
        # initialize vars
        l = 0; r = 0; n = len(s); length = 0

        # interate through right pointer till end
        for r in range(0, len(s)):
            # case 1: dupe found
            if s[r] in tracker:  
            # move left pointer until first instance of the dupe is removed
                while s[l] != s[r]:
                    # remove chars from tracker that weren't dupes but removed
                    tracker.remove(s[l])
                    l+=1
                l+=1

            # case 2: no dupe found
            else:
                tracker.add(s[r])
                
            # measure length after every iteration
            length = max(length, r - l + 1 )

        
        return length