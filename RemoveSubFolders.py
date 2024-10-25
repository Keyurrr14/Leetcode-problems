class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = [folder[0]]
        for i in range(1, len(folder)):
            last = res[-1] + '/'
            if not folder[i].startswith(last):
                res.append(folder[i])
        return res
    
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folderSet = set(folder)
        res = []

        for f in folder:
            res.append(f)
            for i in range(len(f)):
                if f[i] == '/' and f[:i] in folderSet:
                    res.pop()
                    break
        return res