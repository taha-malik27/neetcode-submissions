class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minIndex = ""
        if len(t) > len(s):
            return minIndex
        minL = int(sys.maxsize)
        
        s_map = defaultdict(int)
        t_map = defaultdict(int)
        

        for c in t:
            t_map[c] +=1
        
        need = len(t_map)
        have = 0
        l = 0

        for r in range(0, len(s)):

            s_map[s[r]] += 1

            if t_map[s[r]] and s_map[s[r]] == t_map[s[r]]:
                have+=1
            
            while have == need:
                if minL > r - l + 1:
                    minL = r - l + 1
                    minIndex = (l,r)

                s_map[s[l]] -= 1

                if t_map[s[l]] and s_map[s[l]] < t_map[s[l]]:
                    have -= 1
                l += 1

        return s[minIndex[0]: minIndex[1]+1] if minIndex != "" else minIndex
            
