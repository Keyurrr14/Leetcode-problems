class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for char in t:
            if char in s:
                s = s.replace(char, " ", 1)
            else:
                return char