class Solution(object):
    def removeOccurrences(self, s, part):
        stack = []
        k = len(part)
        
        for ch in s:
            stack.append(ch)
            if len(stack) >= k and "".join(stack[-k:]) == part:
                for _ in range(k):
                    stack.pop()
        
        return "".join(stack)
