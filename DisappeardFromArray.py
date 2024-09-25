class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_nums = set(nums)
        missing = []

        for i in range(1,len(nums)+1):
            if i not in set_nums:
                missing.append(i)

        return missing
    

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        duplicateNums = [0] * (len(nums) + 1)
        res = []
        for i in nums:
            duplicateNums[i] += 1
        for i in range(1, len(nums) + 1):
            if duplicateNums[i] == 0:
                res.append(i)
            
        return res
        