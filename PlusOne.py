class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plusone = int("".join([str(d) for d in digits])) + 1
        return [int(d) for d in str(plusone)]