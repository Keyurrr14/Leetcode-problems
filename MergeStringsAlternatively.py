class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for char in range(min(len(word1), len(word2))):
            res += word1[char]
            res += word2[char]

        if len(word1) > len(word2):
            res += word1[len(word2):]
        else:
            res += word2[len(word1):]
        
        return res