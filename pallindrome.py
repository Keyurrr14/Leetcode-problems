class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        rev = 0
        while temp>0:
            dig = temp%10
            rev = rev*10 + dig
            temp = temp//10
        
        if x == rev:
            return True


