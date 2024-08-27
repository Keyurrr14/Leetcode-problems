class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        sortHeights = sorted(zip(heights, names), reverse = True)
        print(sortHeights)

        res = [name for height, name in sortHeights]
        return res