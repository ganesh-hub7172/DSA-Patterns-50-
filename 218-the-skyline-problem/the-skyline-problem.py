import heapq
from collections import Counter

class Solution:
    def getSkyline(self, buildings):
        events = []
        
        # Create events
        for L, R, H in buildings:
            events.append((L, -H))  # building start
            events.append((R, H))   # building end
        
        # Sort events
        events.sort()
        
        result = []
        heap = [0]                  # max heap (using negatives)
        active = Counter({0: 1})    # height counter
        prev_max = 0
        
        for x, h in events:
            if h < 0:  # start of building
                heapq.heappush(heap, h)
                active[-h] += 1
            else:      # end of building
                active[h] -= 1
            
            # Remove inactive heights
            while heap and active[-heap[0]] == 0:
                heapq.heappop(heap)
            
            curr_max = -heap[0]
            
            if curr_max != prev_max:
                result.append([x, curr_max])
                prev_max = curr_max
        
        return result
