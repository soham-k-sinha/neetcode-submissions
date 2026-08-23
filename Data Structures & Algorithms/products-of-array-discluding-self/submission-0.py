class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i] = prod
            prod *= nums[i]
        
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= prod
            prod *= nums[i]
        
        return result