class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        full = numBottles
        empty = 0
        ans = 0
        need = numExchange

        while full > 0:
            ans += full
            empty += full
            full = 0

            if empty >= need:
                empty -= need
                full += 1
                need += 1

        return ans
