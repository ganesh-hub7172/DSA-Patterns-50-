class Solution:
    def getHappyString(self, n, k):
        total = 3 * (1 << (n - 1))
        if k > total:
            return ""

        k -= 1
        ans = []
        chars = ['a', 'b', 'c']

        for i in range(n):
            block = 1 << (n - i - 1)
            for ch in chars:
                if ans and ch == ans[-1]:
                    continue
                if k >= block:
                    k -= block
                else:
                    ans.append(ch)
                    break

        return "".join(ans)
