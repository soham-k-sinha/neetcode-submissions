class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # We have to count frequencies for each element, I'm thinking hashmap for the frequencies
        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
        # That is be a O(n) pass over nums to count the frequencies of every element in nums

        # I have frequencies, I could sort the elements in the hashmap by the frequencies in reverse order (values) and return the first k elements
        # However this is O(n log n) because we sort and in the worst case hashmap has size n (all elements in nums are distinct)

        # Instead I could try using an array to store frequencies and use the indices as the frequencies and the array itself store lists of the numbers with that frequency
        arr =  [[] for i in range(len(nums) + 1)] # I'm adding len(nums) empty lists because the max frequency an element can have in an array is len(nums) and lowest is 1 (technnically 0 but we don't count that because it's not in the list then)
        for n, i in hashmap.items():
            arr[i].append(n) # adding number n to it's respective frequency index
        
        result = []
        for i in range(len(arr) - 1, 0, -1):
            for n in arr[i]:
                result.append(n)
            
            if len(result) == k:
                return result
        