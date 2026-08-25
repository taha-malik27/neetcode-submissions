class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower() #make it all lower case
        s = "".join(c for c in s if c.isalnum()) # remove non alpha numerics
        
        for i in range(0,int(len(s)/2)): # int works here as .5's truncation only happens on odds, and with odds, 
                                         # the middle character never needs to be checked as it cant invalidate a palindrome (symmetry)
            front = s[i]
            back = s[len(s) - i - 1] 
            if front != back:
                return False
        
        return True
