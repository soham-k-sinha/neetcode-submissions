class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for n in nums:
            hashmap[n] += 1

        a = sorted(list(hashmap.items()), reverse = True, key = lambda x: x[1])[:k]
        return [x[0] for x in a]