class Solution:
    def mySqrt(self, x: int) -> int:
        return int(x**0.5)
    
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid < x:
                left = mid + 1
            elif mid * mid > x:
                right = mid -1
            else:
                return mid
            
        return right

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x

        while left <= right:
            mid = (left + right) // 2
            midSquared = mid * mid
            if midSquared == x:
                return mid
            elif midSquared < x:
                left = mid  + 1
            else:
                right = mid - 1
        return right