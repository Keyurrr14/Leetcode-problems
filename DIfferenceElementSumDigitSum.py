class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = word.find(ch)
        if i != -1:
            return word[:i+1][::-1] + word[i+1:]
        return word
    
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elemSum = sum(nums)
        digitSum = 0
        for i in nums:
            while i != 0:
                digit = i % 10
                digitSum += digit
                i //= 10
        return abs(elemSum - digitSum)