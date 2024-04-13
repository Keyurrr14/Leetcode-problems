class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: 
            return s

        res = ""
        for row in range(numRows):
            increment = (numRows - 1) * 2
            for i in range(row, len(s), increment):
                res += s[i]
                if (row>0 and row<numRows-1 and (i+increment-2*row)<len(s)):
                    res += s[i+increment-2*row]
        
        return res

# increment is kinda the basic formula that helps us understand where the next character arrives in the row
# first and the last row have the charaters at the same place
# the middle rows have some intermediate characters that needs to be included. these characters arrive at -2*row position. hence the if condition takes cares of the middle rows