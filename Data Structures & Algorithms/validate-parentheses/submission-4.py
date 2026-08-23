class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []
        for ch in s:
            if ch in closeToOpen.values():
                stack.append(ch)
            else:
                if stack and closeToOpen[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return not stack