class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return int(num ** 0.5) * int(num ** 0.5) == num
    
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num

        while left <= right:
            mid = (left + right) // 2
            midSquared = mid * mid

            if midSquared == num:
                return True
            elif midSquared < num:
                left = mid + 1
            else:
                right = mid - 1
            
        return False