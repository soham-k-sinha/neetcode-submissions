class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # set(s[l:r]), if s[r] is not in set, r+=1
        # if s[r] is in set, l=r, r+=1
        if len(s) == 0:
            return 0
        
        max_len = 1
        l, r = 0, 1
        while r < len(s):
            string_set = set(s[l:r])
            print(string_set)
            if s[r] in string_set:
                l+=1
            else:
                max_len = max(max_len, r-l+1)
                r+=1
        return max_len