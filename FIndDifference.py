class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for char in t:
            if char in s:
                s = s.replace(char, " ", 1)
            else:
                return char
            
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sumS = sum(ord(i) for i in s)
        sumT = sum(ord(j) for j in t)
        return chr(sumT - sumS)