class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        result = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

        for j in range(len(word2) + 1):
            result[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            result[i][len(word2)] = len(word1) - i

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    result[i][j] = result[i+1][j+1]
                else:
                    result[i][j] = 1 + min(result[i+1][j], result[i][j+1], result[i+1][j+1])

        return result[0][0]