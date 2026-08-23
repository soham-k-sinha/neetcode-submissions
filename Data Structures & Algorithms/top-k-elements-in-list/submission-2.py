class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            hashmap[n] += 1
        
        for elem, f in hashmap.items():
            freq[f].append(elem)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for elem in freq[i]:
                res.append(elem)
                if len(res) == k:
                    return res

        