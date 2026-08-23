class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # I would like to go through the array and replace each element with it's preceeding product, for example at index i, I would like to multiply nums[i] with nums[:i] and store that.
        # I can do this by keeping track of every preceeding product and just update (multiply) it with the upcoming element.
        # Then I want to do the same thing, but in reverse order, this allows me to store the product of every element except nums[i] at i

        forward = nums.copy()
        forward[0] = 1
        prod = 1
        for i in range(1, len(nums)):
            prod *= nums[i-1]
            forward[i] = prod
            # forward for the first example Input: nums = [1,2,4,6] becomes forward = [1, 1, 2, 8]
        # [4, ]
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            forward[i] *= prod
            prod *= nums[i]
        return forward


        # This solution is O(2n) time so hence O(n) time and O(n) space because of the forward array that was a copy of nums