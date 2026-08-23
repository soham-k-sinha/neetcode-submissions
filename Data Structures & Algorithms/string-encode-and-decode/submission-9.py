class Solution:

    def encode(self, strs: List[str]) -> str:
        st = ""
        for i in strs:
            a = i + "™"
            st += a
        return st

    def decode(self, s: str) -> List[str]:
        no_ls = [i for i in range(len(s)) if s[i] == "™"]
        no = 0
        ls = []
        for i in no_ls:
            ls.append(s[no:i])
            no = i + 1
        return ls
        
 