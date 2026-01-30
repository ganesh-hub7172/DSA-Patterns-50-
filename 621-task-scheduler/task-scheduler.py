from collections import Counter

class Solution:
    def leastInterval(self, tasks, n):
        freq = Counter(tasks)
        max_freq = max(freq.values())
        max_count = 0

        for v in freq.values():
            if v == max_freq:
                max_count += 1

        intervals = (max_freq - 1) * (n + 1) + max_count

        return max(intervals, len(tasks))
