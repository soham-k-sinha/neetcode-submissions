class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphaS = "".join(a.lower() for a in s if a.isalnum())
        left = 0
        right = len(alphaS) - 1
        while left < right:
            if alphaS[left] != alphaS[right]:
                return False
            left += 1
            right -= 1
        return True
        