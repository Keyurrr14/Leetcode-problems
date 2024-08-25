class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        res = 0
        for i, j in zip(sorted(seats), sorted(students)):
            res += abs(i - j)
        return res
        

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        res = 0
        seats.sort()
        students.sort()
        for i in range(len(seats)):
            res += abs(seats[i] - students[i])
        return res
        