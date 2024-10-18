class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        negative = (dividend < 0) != (divisor < 0)
        
        absDividend = abs(dividend)
        absDivisor = abs(divisor)
        
        result = 0
        while absDividend >= absDivisor:
            temp = absDivisor
            multiple = 1
            while absDividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            absDividend -= temp
            result += multiple
        
        if negative:
            result = -result
        
        return max(min(result, 2**31 - 1), -2**31)
