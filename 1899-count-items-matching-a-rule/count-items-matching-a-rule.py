class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        idx = 0 if ruleKey == "type" else 1 if ruleKey == "color" else 2
        return sum(1 for item in items if item[idx] == ruleValue)
