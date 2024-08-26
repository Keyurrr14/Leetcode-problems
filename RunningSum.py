class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = 0
        right = sum(nums)
        res = []
        
        for i in range(len(nums)):
            right -= nums[i]
            res.append(abs(left - right))
            left += nums[i]
        return res
    
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        sum = 0
        for i in nums:
            sum += i
            res.append(sum)
        return res
    
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums