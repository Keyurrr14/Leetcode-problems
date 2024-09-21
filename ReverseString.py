class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left <= right:
            charAtLeft = s[left]
            charAtRight = s[right]

            s[left] = charAtRight
            s[right] = charAtLeft

            left += 1
            right -= 1
        
        return s
    
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left <= right:
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1
        
        return s
    
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        newString = s[::-1]
        s.clear()
        for char in newString:
            s.append(char)