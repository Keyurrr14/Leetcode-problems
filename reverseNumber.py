class Solution:
    def reverse(self, x: int) -> int:
        stringRev = str(abs(x))
        stringRev = stringRev.strip()
        stringRev = stringRev[::-1]
        
        result = int(stringRev)
        
        if result >= 2** 31 -1 or result <= -2** 31:
            return 0
        elif x < 0:
            return -1 * result
        else:
            return result
        