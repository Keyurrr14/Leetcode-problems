class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        l1 = "qwertyuiop"
        l2 = "asdfghjkl"
        l3 = "zxcvbnm"
        res = []
        for word in words:
            w = word.lower()
            if len(set(l1 + w)) == len(l1) or len(set(l2 + w)) == len(l2) or len(set(l3 + w)) == len(l3):
                res.append(word)
        
        return res


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        l1 = "qwertyuiop"
        l2 = "asdfghjkl"
        l3 = "zxcvbnm"
        res = []
        for word in words:
            w = set(word.lower())
            if w.issubset(l1) or w.issubset(l2) or w.issubset(l3): 
                res.append(word)
        
        return res