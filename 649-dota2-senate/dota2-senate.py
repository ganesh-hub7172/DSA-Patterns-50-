from collections import deque

class Solution:
    def predictPartyVictory(self, senate):
        n = len(senate)
        radiant = deque()
        dire = deque()

        # Initialize the queues with indices
        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        # Simulate the rounds
        while radiant and dire:
            r_index = radiant.popleft()
            d_index = dire.popleft()
            
            # Senator with smaller index bans the other
            if r_index < d_index:
                radiant.append(r_index + n)  # Radiant goes to next round
            else:
                dire.append(d_index + n)     # Dire goes to next round

        return "Radiant" if radiant else "Dire"
