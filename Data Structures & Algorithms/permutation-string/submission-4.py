class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        s1Count = {}
        s2Count = {}

        for i in range(len(s1)):
            s1Count[s1[i]] = s1Count.get(s1[i], 0) + 1
            s2Count[s2[i]] = s2Count.get(s2[i], 0) + 1

        l = 0

        for r in range(len(s1), len(s2)):
            if s1Count == s2Count: return True
            s2Count[s2[r]] = s2Count.get(s2[r], 0) + 1
            if s2Count[s2[l]] == 1:
                s2Count.pop(s2[l])
            else:
                s2Count[s2[l]] -= 1
            l+=1
        return s1Count == s2Count