class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        digitSum = sum(int(n) for n in str(x))

        return digitSum if x%digitSum == 0 else -1
    
