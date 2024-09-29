class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for j in range(len(t)):
            if i < len(s) and s[i] == t[j]:
                i += 1
        return i == len(s)


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
            
        return len(s) == i