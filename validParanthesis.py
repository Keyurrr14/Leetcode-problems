class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paranthesis_map = {
            ")" : "(",
            "}" : "{",
            "]" : "[",
        }
        open_paranthesis = set(["(", "{", "["])

        for i in s:
            if i in open_paranthesis:
                stack.append(i)
            elif stack and stack[-1] == paranthesis_map[i]:
                stack.pop()
            else:
                return False
        
        return stack == []