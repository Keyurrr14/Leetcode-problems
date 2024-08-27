class Solution:
    def pivotInteger(self, n: int) -> int:
        counter = -1
        lst = [i for i in range(1, n+1)]

        for i in range(len(lst)):
            if sum(lst[0:i+1]) == sum(lst[i:]):
                counter = i + 1
        return counter