class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def CombinationsII(i, curr, total):
            if target == total:
                res.append(curr.copy())
                return
            elif i == len(candidates) or total > target:
                return

            curr.append(candidates[i])
            CombinationsII(i + 1, curr, total + candidates[i])
            curr.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            CombinationsII(i + 1, curr, total)
        
        CombinationsII(0, [], 0)

        return res