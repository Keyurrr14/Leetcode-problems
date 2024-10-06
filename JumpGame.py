class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumps = 0
        for n in nums:
            if jumps < 0:
                return False
            elif n > jumps:
                jumps = n
            jumps -= 1

        return True  