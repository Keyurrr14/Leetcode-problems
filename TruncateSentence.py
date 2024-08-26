class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        lst = s.split(" ")
        res = []
        for i in range(k):
            res.append(lst[i])
        return " ".join(res)