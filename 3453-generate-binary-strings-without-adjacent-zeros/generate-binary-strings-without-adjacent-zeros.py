class Solution:
    def validStrings(self, n):
        result = []

        def backtrack(s):
            if len(s) == n:
                result.append(s)
                return

            # Always allowed to add '1'
            backtrack(s + "1")

            # Add '0' only if previous char is not '0'
            if not s or s[-1] == '1':
                backtrack(s + "0")

        backtrack("")
        return result
