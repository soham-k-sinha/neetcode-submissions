class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # target - n: (n, i)
        # hashmap will contain the element to find 
        for i, n in enumerate(nums):
            if n in hashmap:
                return [hashmap[n][1], i]
            diff = target - n
            hashmap[diff] = (n, i)
        
