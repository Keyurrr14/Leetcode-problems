class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def MatchingParanthesis(openN, closedN):
            if openN == closedN == n:
                return result.append("".join(stack))
            
            if openN < n:
                stack.append("(")
                MatchingParanthesis(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                MatchingParanthesis(openN, closedN + 1)
                stack.pop()

        MatchingParanthesis(0, 0)
        return result
        
