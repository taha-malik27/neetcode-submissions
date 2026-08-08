class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = {}
        t_counter = {}
        s_array = list(s)
        t_array = list(t)
        
        # first get character counter for s string
        for s_c in s_array:
            if s_counter.get(s_c) == None:
                s_counter[s_c] = 1
            else:
                s_counter[s_c] +=1
        
        #  get character counter for t string
        for t_c in t_array:
            if t_counter.get(t_c) == None:
                t_counter[t_c] = 1
            else:
                t_counter[t_c] += 1
        
        # if length not equal guaranteed not anagram so return false early
        if len(t_counter) != len(s_counter):
            return False
        # if same length, do o(n) check on each key to compare if their counters are identical, if they dont have same keys but same length, also caught here as get() will return None.
        else:
            for key in s_counter:
                if s_counter.get(key) != t_counter.get(key):
                    return False
        return True
                

        
