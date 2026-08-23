class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # set(s[l:r]), if s[r] is not in set, r+=1
        # if s[r] is in set, l=r, r+=1
        if len(s) == 0:
            return 0
        
        max_len = 1
        l, r = 0, 1
        string_set = set(s[l])
        while r < len(s):
            if s[r] in string_set:
                string_set.remove(s[l])
                l+=1
            else:
                string_set.add(s[r])
                max_len = max(max_len, r-l+1)
                r+=1

        return max_len