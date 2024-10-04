class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return f"{int(date[0:4]):b}-{int(date[5:7]):b}-{int(date[8:10]):b}"
    

class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return "-".join(f"{int(d):b}" for d in date.split("-"))