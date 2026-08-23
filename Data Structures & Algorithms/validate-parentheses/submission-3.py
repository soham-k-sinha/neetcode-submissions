class Solution:
    from collections import deque
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
                if stack and stack[-1] == closeToOpen[ch]:
                    stack.pop()
                    continue
                else:
                    return False
        return not stack
                
