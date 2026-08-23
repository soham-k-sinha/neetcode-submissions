class Solution:
    def isPalindrome(self, s: str) -> bool:
        # I can use a 2 pointer approach, starting off from the extremes of the string, I check if each character is the same one by one
        # I can have a left and right pointer, check if they're the same at every step, until left pointer exceeds right
        # There can be an issue with alphanumeric characters and we can avoid this by looping l and r until we get the next alphanumeric character

        l, r = 0, len(s) - 1
        while l < r:
            while not s[l].isalnum() and l < r:
                l += 1
            while not s[r].isalnum() and l < r:
                r-=1
            
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True