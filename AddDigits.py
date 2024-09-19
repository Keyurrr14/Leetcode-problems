class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0: return 0
        if num % 9 == 0: return 9
        else: return (num % 9)

class Solution:
    def addDigits(self, num: int) -> int:
        res = 0
        while num > 9:
            newNum = str(num)
            num = sum(res + int(i) for i in newNum)
        return num