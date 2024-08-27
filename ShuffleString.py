class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = ""
        for i in range(len(s)):
            res += s[indices.index(i)]
        return res
    
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [""] * len(indices)
        for character, i in zip(s, indices):
            res[i] = character
        return "".join(res)