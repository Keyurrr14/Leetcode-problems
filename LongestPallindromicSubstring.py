class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd length
            l = r = i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l-=1
                r+=1
            
            # even length
            l, r = i, i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l-=1
                r+=1
        
        return res
    
# we basically select a character and check the character at left and right position. if they are equal then expand outwards by decrementing the left and incrementing the right
# the first 2 condtitions in while loop keeps the left and right pointer in bound
# the third condition checks the character at left and right position