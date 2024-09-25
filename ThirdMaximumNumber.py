class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sortedList = sorted(list(set(nums)))
        if len(sortedList) < 3:
            return sortedList[-1]
        else:
            return sortedList[-3]


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        newNums = set(nums)
        if len(newNums) < 3:
            return max(newNums)
        else:
            newNums.remove(max(newNums))
            newNums.remove(max(newNums))
            return max(newNums)