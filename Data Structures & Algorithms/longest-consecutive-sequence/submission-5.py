class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # I'm thinking I could go through every element in nums and look at if nums[i] - 1 exists in nums (using a set of nums to allow for quick O(1) lookup)
        # At every iteration i keep track of max_length I've seen so far, if it is then I update it
        # If a sequence breaks I reset my current counter for length of sequence back to 0
        # And we iterate through numSet, not nums because nums may have duplicates and we don't want to double count them into our sequence
        
        max_length = 0
        numSet = set(nums)
        for i in numSet:
            curr_length = 1
            curr = i
            while (curr-1) in numSet:
                curr_length += 1
                curr -= 1
            max_length = max(max_length, curr_length)
        return max_length

    '''
    dry run:
        Input: nums = [2,20,4,10,3,4,5]
        numSet = [2, 20, 4, 10, 3, 5]
        1 in numSet? No, curr_length = 1
        19 in numSet? No, curr_length = 1
        3 in numSet? Yes, curr_length = 2, max_length = 2
        2 in numSet? Yes, curr_length = 3, max_length = 3
        1 in numSet? No, curr_length = 1
        9 in numSet? No, curr_length = 1
        2 in numSet? Yes, curr_length = 2
        1 in numSet? No, curr_length = 1
        4 in numSet? Yes, curr_length = 2
        3 in numSet? Yes, curr_length = 3
        2 in numSet? Yes, curr_length = 4, max_length = 4
        1 in numSet? No
        exit
    '''