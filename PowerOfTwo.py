class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(31):
            res = 2 ** i
            if res == n:
                return True
        return False