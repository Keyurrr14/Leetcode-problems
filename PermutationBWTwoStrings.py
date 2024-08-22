class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        diff = 0
        for char in set(s):
            indexS = s.index(char)
            indexT = t.index(char)
            diff += abs(indexS - indexT)
        return diff