class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False # initial check for easy case of false
        
        sd = {}
        td = {}

        for sc, tc in zip(s,t):
            if sd.get(sc) ==None:
                sd[sc] = 1
            else:
                sd[sc] += 1

            if td.get(tc) == None:
                td[tc] = 1
            else: 
                td[tc] +=1
        
        return sd == td
    
