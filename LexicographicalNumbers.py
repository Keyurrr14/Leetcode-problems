class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        def dfs(curr):
            if curr > n:
                return
            res.append(curr)
            for i in range(10):
                dfs(curr * 10 + i)
        
        for i in range(1, 10):
            dfs(i)
            
        return res
    

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        curr = 1
        while len(res) < n:
            res.append(curr)
            if curr * 10 <= n:
                curr = curr * 10
            else:
                while curr == n or curr % 10 == 9:
                    curr = curr // 10
                curr = curr + 1
        
        return res