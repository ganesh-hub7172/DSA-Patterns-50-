import heapq
import math

class Solution:
    def pickGifts(self, gifts, k):
        heap = [-g for g in gifts]
        heapq.heapify(heap)

        for _ in range(k):
            x = -heapq.heappop(heap)
            x = int(math.sqrt(x))
            heapq.heappush(heap, -x)

        return -sum(heap)