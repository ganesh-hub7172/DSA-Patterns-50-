class Solution:
    def sortPeople(self, names, heights):
        return [name for _, name in sorted(zip(heights, names), reverse=True)]
