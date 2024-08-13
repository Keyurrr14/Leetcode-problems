class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def Combinations(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            
            if i >= len(candidates) or total > target:
                return

            curr.append(candidates[i])
            Combinations(i, curr, total + candidates[i])
            curr.pop()
            Combinations(i + 1, curr, total)
        
        Combinations(0, [], 0)
        return res