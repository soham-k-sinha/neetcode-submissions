class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        words = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in words:
                words[sorted_word].append(word)
            else:
                words[sorted_word] = [word]
        return list(words.values())