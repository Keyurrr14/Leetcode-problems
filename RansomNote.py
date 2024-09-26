class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineMap = {}
        for char in magazine:
            if char in magazineMap:
                magazineMap[char] += 1
            else:
                magazineMap[char] = 1
        
        for char in ransomNote:
            if char not in magazineMap:
                return False
            elif magazineMap[char] == 1:
                del magazineMap[char]
            else:
                magazineMap[char] -= 1
        
        return True
    

from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineMap = Counter(magazine)

        for char in ransomNote:
            if char not in magazineMap:
                return False
            elif magazineMap[char] == 1:
                del magazineMap[char]
            else:
                magazineMap[char] -= 1
        
        return True