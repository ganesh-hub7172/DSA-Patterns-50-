import heapq

class MedianFinder:
    def __init__(self):
        # max heap (invert values for Python)
        self.left = []
        # min heap
        self.right = []

    def addNum(self, num):
        # push to max heap
        heapq.heappush(self.left, -num)

        # balance: largest of left goes to right
        heapq.heappush(self.right, -heapq.heappop(self.left))

        # keep size property
        if len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self):
        if len(self.left) > len(self.right):
            return float(-self.left[0])
        return (-self.left[0] + self.right[0]) / 2.0
