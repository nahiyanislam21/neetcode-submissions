class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {')': '(',
         '}': '{',
          ']': '['}
        for char in s:
            if char in match:
                if stack and stack[-1] == match[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
