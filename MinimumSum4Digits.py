class Solution:
    def minimumSum(self, num: int) -> int:
        num = sorted(str(num), reverse = True)
        return int(num[0]) + int(num[1]) + int(num[2])*10 + int(num[3])*10
    

class Solution:
    def minimumSum(self, num: int) -> int:
        digits = [None] * 4
        for i in range(4):
            digits[i] = num % 10
            num //= 10
        digits.sort()
        return (digits[0] + digits[1])*10 + digits[2] + digits[3]