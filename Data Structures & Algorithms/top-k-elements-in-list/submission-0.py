from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_buckets = {freq: list() for freq in range(1, len(nums)+1)}
        freq_counter = defaultdict(int)
        k_list = []

        # first grab all frequencies of numbers (O(n))
        for num in nums:
            freq_counter[num] += 1

        # next put all the finalized frequencies into their respective buckets (O(n))
        for key in freq_counter.keys():
            freq_buckets[freq_counter[key]].append(key)

        # iterate backwards in freq_buckets, collect k items (O(k) and k <= n)
        for bucket in range(len(nums), 0,-1):
            k_list.extend(list(freq_buckets[bucket]))
            if len(k_list) == k: #since we know its unique, dont have to worry about list length overshooting k
                return k_list

                


        
