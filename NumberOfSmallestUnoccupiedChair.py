class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        times = [(t[0], t[1], i) for i, t in enumerate(times)]
        times.sort()

        usedChair = []
        availableChairs = [i for i in range(len(times))]

        for a, l, i in times:
            while usedChair and usedChair[0][0] <= a:
                leave, chair = heapq.heappop(usedChair)
                heapq.heappush(availableChairs, chair)

            chair = heapq.heappop(availableChairs)
            heapq.heappush(usedChair, (l, chair))

            if i == targetFriend:
                return chair