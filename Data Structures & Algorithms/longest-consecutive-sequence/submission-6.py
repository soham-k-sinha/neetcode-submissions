class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # I'm thinking I could go through every element in nums and look at if nums[i] - 1 exists in nums (using a set of nums to allow for quick O(1) lookup)
        # At every iteration i keep track of max_length I've seen so far, if it is then I update it
        # If a sequence breaks I reset my current counter for length of sequence back to 0
        # And we iterate through numSet, not nums because nums may have duplicates and we don't want to double count them into our sequence
        
        max_length = 0
        numSet = set(nums)
        for i in numSet:
            if i-1 not in numSet:
                curr_length = 1
                curr = i
                while (curr+1) in numSet:
                    curr_length += 1
                    curr += 1
                max_length = max(max_length, curr_length)
        return max_length
