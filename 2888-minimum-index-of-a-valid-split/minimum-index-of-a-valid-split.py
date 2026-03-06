class Solution:
    def minimumIndex(self, nums):
        from collections import Counter
        
        n = len(nums)
        count = Counter(nums)
        dom = max(count, key=count.get)
        total = count[dom]

        left_count = 0

        for i in range(n - 1):
            if nums[i] == dom:
                left_count += 1

            left_len = i + 1
            right_len = n - left_len
            right_count = total - left_count

            if left_count > left_len // 2 and right_count > right_len // 2:
                return i

        return -1