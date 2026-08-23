class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # I could create a fixed window of length len(s1) and slide through s2, every substring within s2 should be checked if it is a permutation of s1
        # 
        
        len_of_window = len(s1)

        s1_freq = {}
        for i in s1:
            s1_freq[i] = s1_freq.get(i, 0) + 1

        l = 0
        for r in range(l + len_of_window - 1, len(s2)):
            subs = s2[l: r+1]
            curr_perm = {}
            for i in subs:
                curr_perm[i] = curr_perm.get(i, 0) + 1
            if curr_perm == s1_freq:
                return True
            l+=1
        return False
