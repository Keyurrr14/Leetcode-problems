class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for char in stones:
            if char in jewels:
                count += 1
        return count
    

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        jewelsSet = set([i for i in jewels])
        for s in stones:
            if s in jewels: count += 1
        
        return count