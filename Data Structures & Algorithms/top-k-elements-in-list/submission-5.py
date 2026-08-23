class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        '''
        count frequencies of elements in a hashmap
        freq = array of length len(nums) + 1 of lists
        the indices of freq are the freq of an element
        the elements of freq are lists containing all the elements that have the same frequency as the index of the position it's at
        then we go through each element in nums and add it to freq appropriately
        then we go through freq backwards and add it to our result array until the length of our result array is k
        '''
        
        hashmap = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            hashmap[n] += 1
        
        for elem, f in hashmap.items():
            freq[f].append(elem)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res