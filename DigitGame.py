class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        singleSum = sum(x for x in nums if x>=1 and x<=9)
        doubleSum = sum(y for y in nums if y>=10)
        return True if (singleSum>doubleSum or doubleSum>singleSum) else False
    
class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        alice = 0
        bob = 0
        for i in nums:
            if len(str(i)) == 1:
                alice += i
            else:
                bob += i
        return alice != bob