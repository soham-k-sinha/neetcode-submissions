class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Instead of counting frequencies in a hashmap, we can store frequencies in a bitmap of size 26 to allow for easier hashability
        # I will also store all the groups of anagrams as a hashmap indexed by the tuple of the frequency bitmap and the values would be lists of the strings in that group
        # This is better than using the sorted string as the key for the group dict as that would be O(klogk) for sorting the strings every time, where k is the length of the string
        # This solution is O(n * k) time where n is the length of strs and k is the length of the longest string
        # O(n) space because there could be n distinct anagrams in strs which makes group size of n, bitmap is O(1) space because it is of constant size everytime.
        group = defaultdict(list)

        for s in strs:
            bitmap = [0] * 26
            for c in s:
                bitmap[ord(c) - ord('a')] += 1
            group[tuple(bitmap)].append(s)
        return list(group.values())


