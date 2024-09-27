class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seenLetters = []
        for char in s:
            if char in seenLetters:
                return char
            else:
                seenLetters.append(char)

