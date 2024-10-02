class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) < 2:
            return False
        
        doubleString = s + s
        res = doubleString[1:-1]
        if s in res: return True
        else: return False