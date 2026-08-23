class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1 = {}
        h2 = {}

        for c in s:
            if c in h1:
                h1[c] += 1
            else:
                h1[c] = 1
        
        for c in t:
            if c in h2:
                h2[c] += 1
            else:
                h2[c] = 1
        return h1 == h2