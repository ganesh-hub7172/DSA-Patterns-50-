class Solution:
    def findRelativeRanks(self, score):
        n = len(score)
        result = [""] * n

        indices = list(range(n))
        indices.sort(key=lambda i: score[i], reverse=True)

        for rank, idx in enumerate(indices):
            if rank == 0:
                result[idx] = "Gold Medal"
            elif rank == 1:
                result[idx] = "Silver Medal"
            elif rank == 2:
                result[idx] = "Bronze Medal"
            else:
                result[idx] = str(rank + 1)

        return result
