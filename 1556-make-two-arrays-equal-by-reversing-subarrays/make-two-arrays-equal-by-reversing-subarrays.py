class Solution:
    def canBeEqual(self, target, arr):
        count = {}

        for x in target:
            count[x] = count.get(x, 0) + 1

        for x in arr:
            if x not in count:
                return False
            count[x] -= 1
            if count[x] < 0:
                return False

        return True