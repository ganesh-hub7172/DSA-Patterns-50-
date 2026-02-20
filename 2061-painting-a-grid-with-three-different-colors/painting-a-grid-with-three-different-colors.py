class Solution:
    def colorTheGrid(self, m, n):
        MOD = 10**9 + 7
        from itertools import product

        states = []
        for col in product(range(3), repeat=m):
            valid = True
            for i in range(1, m):
                if col[i] == col[i - 1]:
                    valid = False
                    break
            if valid:
                states.append(col)

        compat = {}
        for s1 in states:
            compat[s1] = []
            for s2 in states:
                ok = True
                for i in range(m):
                    if s1[i] == s2[i]:
                        ok = False
                        break
                if ok:
                    compat[s1].append(s2)

        dp = {s: 1 for s in states}

        for _ in range(1, n):
            new_dp = {}
            for s in states:
                total = 0
                for prev in compat[s]:
                    total = (total + dp[prev]) % MOD
                new_dp[s] = total
            dp = new_dp

        return sum(dp.values()) % MOD
