class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count = []
        for word in sentences:
            count.append(word.count(' ')+1)
        return max(count)
    

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count = 0
        for word in sentences:
            wordlen = len(word.split())
            if wordlen >= count:
                count = wordlen
        return count