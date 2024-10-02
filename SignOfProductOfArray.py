class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = 1
        for i in range(len(nums)):
            res = res * nums[i]
        
        def signFunc(res):
            if res > 0:
                return 1
            elif res < 0:
                return -1
            else:
                return 0
        
        return signFunc(res)
    
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        isNegative = False

        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                isNegative = not isNegative
        
        return -1 if isNegative else 1