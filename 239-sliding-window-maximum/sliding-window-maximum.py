from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()   # stores indices
        result = []

        for i in range(len(nums)):
            # Remove elements out of the window
            if dq and dq[0] == i - k:
                dq.popleft()

            # Remove smaller elements (they can't be max)
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # Start adding results once the window is full
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
