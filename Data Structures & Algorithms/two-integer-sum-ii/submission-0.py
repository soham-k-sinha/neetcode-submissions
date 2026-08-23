class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # We can use brute force for O(1) space but that will be O(n^2) time
        # We should utilize the fact that this array is sorted
        # I'm thinking along the lines of having a 2 pointer approach where we start on the edges of the array and move our pointers according to if the sum is greater than or smaller than our target, similar to binary search but a bit different
        # If the sum of the current numbers is greater than target, we can reduce the sum by shifting the right pointer to the left
        # If the sume of the current numbers is smaller than target, we can increase the sum by shifting the left pointer to the right
        # I'm going to treat the indices as normal but I'll add 1 to them in the end

        l, r = 0, len(numbers) - 1
        while l < r:
            curr_sum = numbers[l] + numbers[r]
            if curr_sum < target:
                # Increase the sum
                l += 1
            elif curr_sum > target:
                # Decrease the sum
                r -= 1
            else:
                return [l+1, r+1]
        # This sol