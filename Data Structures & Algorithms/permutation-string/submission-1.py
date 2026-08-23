class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # I could create a fixed window of length len(s1) and slide through s2, every substring within s2 should be checked if it is a permutation of s1
        
        len_of_window = len(s1)

        s1_freq = {}
        for i in s1:
            s1_freq[i] = s1_freq.get(i, 0) + 1

        l = 0
        curr_perm = {}
        for i in s2[:len_of_window-1]:
            curr_perm[i] = curr_perm.get(i, 0) + 1

        for r in range(len_of_window - 1, len(s2)):
            curr_perm[s2[r]] = curr_perm.get(s2[r], 0) + 1
            if curr_perm == s1_freq:
                return True
            if curr_perm[s2[l]] == 1:
                curr_perm.pop(s2[l])
            else:
                curr_perm[s2[l]] -= 1
            l+=1
        return False

        # Time complexity is O(m * n) where m is the length of s1 and n is the length of s2 but since m is a constant, this is linear time
