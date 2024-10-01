class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        res1 = len(candyType) // 2
        res2 = len(set(candyType))
        return min(res1, res2)

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(set(candyType)), len(candyType) // 2)
    