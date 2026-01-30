class Solution:
    def timeRequiredToBuy(self, tickets, k):
        total_time = 0
        for i, t in enumerate(tickets):
            if i <= k:
                total_time += min(t, tickets[k])
            else:
                total_time += min(t, tickets[k] - 1)
        return total_time
