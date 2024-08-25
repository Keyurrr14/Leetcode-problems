class Solution:
    def balancedStringSplit(self, s: str) -> int:
        countLR, res = 0, 0
        for char in s:
            countLR += 1 if char == 'R' else -1
            if countLR == 0:
                res += 1
        return res
        