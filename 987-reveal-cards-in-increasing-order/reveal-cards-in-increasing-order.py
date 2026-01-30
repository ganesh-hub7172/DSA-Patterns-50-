from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck):
        deck.sort(reverse=True)
        q = deque()

        for card in deck:
            if q:
                q.appendleft(q.pop())
            q.appendleft(card)

        return list(q)
