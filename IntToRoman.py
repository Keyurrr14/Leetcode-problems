class Solution:
    def intToRoman(self, num: int) -> str:
        symList = [
            ["I", 1],
            ["IV", 4],
            ["V", 5],
            ["IX", 9],
            ["X", 10],
            ["XL", 40],
            ["L", 50],
            ["XC", 90],
            ["C", 100],
            ["CD", 400],
            ["D", 500],
            ["CM", 900],
            ["M", 1000]
        ]
        res = ""
        for symbol, value in reversed(symList):
            if num // value:
                count = num // value
                res += (symbol*count)
                num = num % value
        return res
    
# we go in reversed order of the symList
# we divide the input number by the value in symList. the answer of the division gives us the count as of how many times do we need to add the symbol of that value to the result. example: 400//1000 = 0 means no "M"symbol need to be added. example 2500//1000 = 2 means 2"M" symbol needs to be added to the result
# we do modulus division to get rid of the first digit of the input number