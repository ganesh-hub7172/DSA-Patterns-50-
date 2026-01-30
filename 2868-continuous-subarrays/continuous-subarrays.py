from collections import deque

class Solution:
    def continuousSubarrays(self, nums):
        max_q = deque()
        min_q = deque()
        left = 0
        ans = 0

        for right, num in enumerate(nums):
            # Maintain max deque (decreasing)
            while max_q and nums[max_q[-1]] < num:
                max_q.pop()
            max_q.append(right)

            # Maintain min deque (increasing)
            while min_q and nums[min_q[-1]] > num:
                min_q.pop()
            min_q.append(right)

            # Shrink window if max - min > 2
            while nums[max_q[0]] - nums[min_q[0]] > 2:
                left += 1
                if max_q[0] < left:
                    max_q.popleft()
                if min_q[0] < left:
                    min_q.popleft()

            # Add subarrays ending at right
            ans += right - left + 1

        return ans
