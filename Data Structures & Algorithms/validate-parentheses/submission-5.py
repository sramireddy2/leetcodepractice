class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        stack = []
        parmap = {')':'(', '}':'{', ']':'['}

        for c in s:
            if c in parmap:
                if stack and stack[-1] == parmap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
        
        