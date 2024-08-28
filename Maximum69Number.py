class Solution:
    def maximum69Number (self, num: int) -> int:
        string = list(str(num))
        for i in range(len(string)):
            if string[i] == "6":
                string[i] = "9"
                break
        return int("".join(string))