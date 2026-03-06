class Solution:
    def pathInZigZagTree(self, label):
        res = []
        level = 0
        node = label

        while (1 << level) <= node:
            level += 1

        while label >= 1:
            res.append(label)
            start = 1 << (level - 1)
            end = (1 << level) - 1
            label = (start + end - label) // 2
            level -= 1

        return res[::-1]