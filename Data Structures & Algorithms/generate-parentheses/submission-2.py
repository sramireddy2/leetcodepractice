class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def backtrack(opencount, closedcount):
            if opencount == closedcount == n:
                result.append("".join(stack))
                return

            if opencount < n:
                stack.append("(")
                backtrack(opencount + 1, closedcount)
                stack.pop()

            if closedcount < opencount:
                stack.append(")")
                backtrack(opencount, closedcount + 1)
                stack.pop()

        backtrack(0, 0)
        return result
        
        