class Solution:
    def peopleAwareOfSecret(self, n, delay, forget):
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1  # day 1, one person learns the secret

        for day in range(2, n + 1):
            for prev in range(1, day):
                if delay <= day - prev < forget:
                    dp[day] = (dp[day] + dp[prev]) % MOD

        # sum all people who haven’t forgotten by day n
        return sum(dp[max(1, n - forget + 1):n + 1]) % MOD
