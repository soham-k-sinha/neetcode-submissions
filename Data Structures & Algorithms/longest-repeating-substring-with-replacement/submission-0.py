class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = 0
        l, r = 0, 0
        hashmap = defaultdict(int)

        while r < len(s):
            sub = s[l:r+1]
            hashmap[s[r]] += 1

            max_freq = 0
            for _, freq in hashmap.items():
                max_freq = max(max_freq, freq)
            if (r - l + 1) - max_freq <= k:
                res = max(res, r - l + 1)
            else:
                hashmap[s[l]] -= 1
                l+=1
            r+=1
        return res