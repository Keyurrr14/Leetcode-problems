class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        ans = ""
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        decoder = {}
        idx = 0

        for char in key:
            if char != " " and char not in decoder:
                decoder[char] = idx
                idx += 1
        
        for char in message:
            if char == " ":
                ans += " "
            else:
                ans += alphabets[decoder[char]]
        return ans