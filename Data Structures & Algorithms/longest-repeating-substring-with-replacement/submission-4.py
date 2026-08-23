class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        res = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            subs = s[l:r+1]

            max_freq = 0
            for i in count.values():
                max_freq = max(max_freq, i)
            
            if (r - l + 1) - max_freq <= k:
                res += 1
            else:
                count[s[l]] -= 1
                l += 1
        return res
