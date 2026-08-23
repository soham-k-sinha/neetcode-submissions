class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s1, f = nums[0], nums[0]
        while True:
            s1 = nums[s1]
            f = nums[f]
            f = nums[f]

            if s1 == f:
                break
        
        s2 = nums[0]
        while s1 != s2:
            s1 = nums[s1]
            s2 = nums[s2]
        return s2
        
        