from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list) # external map that puts strings into buckets based on the freq of their chars.
        
        for string in strs:  
            str_counter = defaultdict(int) # internal counter for counting chars in each string

            for c in string:   # despite nested loop, its still m*n complexity
                str_counter[c] += 1  # counter for current string, defaultdict takes handles no key
            signature = frozenset(str_counter.items()) # convert str_counter to a signature for outter hashmap to use as key
            anagram_map[signature].append(string) #append string if its dict counter matches an existing on, defaultdict handles no key with empty list, exactly what we want.
        
        return(list(anagram_map.values())) #dicts values wraps its own type despite it structually storing a list, so just use list()
