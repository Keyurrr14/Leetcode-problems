class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)

        for i in s:
            count[i] += 1
        
        for i in t:
            count[i] -= 1

        for val in count.values():
            if val != 0:
                return False
            
        return True