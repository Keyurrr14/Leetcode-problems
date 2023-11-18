class Solution:
    def romanToInt(self, s: str) -> int:
        rom_to_int = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }

        num = 0
        last = "I"

        for i in s[::-1]:
            if rom_to_int[i] < rom_to_int[last]:
                num -= rom_to_int[i]
            else:
                num += rom_to_int[i]
            last = i

        return num