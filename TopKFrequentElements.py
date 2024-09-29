class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        minHeap = []
        for key, val in count.items():
            heapq.heappush(minHeap, (val, key))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return [item[1] for item in minHeap]


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freqVal = {}
        for n in nums:
            freqVal[n] = 1 + freqVal.get(n, 0)
        
        for key, val in freqVal.items():
            heapq.heappush(heap, (-val, key))
        
        res = []
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])
        
        return res