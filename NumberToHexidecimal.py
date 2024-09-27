class Solution:
    def toHex(self, num: int) -> str:
        res = []
        hexaDecimal = "0123456789abcdef"
        if num == 0:
            return "0"
        elif num > 0 and num <= 15:
            return hexaDecimal[num]
        if num < 0:
            num += 2**32
        while num > 0:
            res.append(hexaDecimal[num % 16])
            num //= 16
        
        return "".join(res[::-1])