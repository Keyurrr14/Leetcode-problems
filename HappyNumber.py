class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def nextNumbers(n):
            res = 0
            while n:
                digit = n % 10
                res += digit ** 2
                n = n // 10
            return res
        
        while n not in seen:
            seen.add(n)
            n = nextNumbers(n)
            if n == 1:
                return True
        return False
    
