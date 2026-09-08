class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tracker = set()
        max_substring = 0
        n = len(s)
        l = 0
        r = 0

        while r < n:
            if s[r] not in tracker:
                tracker.add(s[r])
            else:
                while s[l] != s[r]:
                    tracker.remove(s[l])
                    l += 1
                l+=1

            substring = r - l + 1
            max_substring = max(max_substring, substring)
            r+=1
        return(max_substring)



        