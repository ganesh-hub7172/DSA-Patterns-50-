class Solution:
    def topKFrequent(self, nums, k):
        # Step 1: Count frequency
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        # Step 2: Buckets where index = frequency
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            buckets[count].append(num)

        # Step 3: Collect top k frequent elements
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
