class Solution:
    def finalString(self, s: str) -> str:
        res = ""
        for char in s:
            if char != "i":
                res += char
            else:
                res = res[::-1]
        return res