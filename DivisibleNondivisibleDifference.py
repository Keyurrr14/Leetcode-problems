class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1, num2 = 0, 0
        for i in range(1,n+1):
            if((i%m) == 0):
                num2 += i
            else:
                num1 += i
        return num1 - num2
    
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = []
        num2 = []
        for i in range(1,n+1):
            if((i%m) == 0):
                num2.append(i)
            else:
                num1.append(i)
        return sum(num1) - sum(num2)