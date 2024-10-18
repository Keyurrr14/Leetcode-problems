class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        d = set(permutations(nums))
        return [list(x) for x in d]
