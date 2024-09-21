class Solution:
    def firstUniqChar(self, s: str) -> int:
        charCount = {}
        for char in s:
            if char not in charCount:
                charCount[char] = 0
            charCount[char] += 1

        for i in range(len(s)):
            if charCount[s[i]] == 1:
                return i
        return -1
    
