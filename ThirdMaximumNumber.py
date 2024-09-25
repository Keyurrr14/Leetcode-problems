class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sortedList = sorted(list(set(nums)))
        if len(sortedList) < 3:
            return sortedList[-1]
        else:
            return sortedList[-3]
