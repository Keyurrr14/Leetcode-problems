class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            res.append(len([j for j in nums if j < i]))
        return res