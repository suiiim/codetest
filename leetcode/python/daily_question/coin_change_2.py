from typing import List

"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.
You may assume that you have an infinite number of each kind of coin. The answer is guaranteed to fit into a signed 32-bit integer.
"""


class Solution:
    # Runtime 263 ms -> 63.55%
    # Memory 17.48 MB -> 99.52%
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1

        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in sorted(coins):
            for i in range(1, amount + 1):
                if i < coin:
                    pass
                elif i == coin:
                    dp[i] += 1
                else:
                    dp[i] += dp[i - coin]

        return dp[amount]

    # Runtime 191 ms -> 86.4%
    # Memory 17.51 MB -> 98.66%
    def change2(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1

        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in sorted(coins):
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[amount]


a = Solution()
print(a.change(amount=5, coins=[5, 2, 1]))  # 4
print(a.change(amount=3, coins=[2]))  # 0
print(a.change(amount=10, coins=[10]))  # 1
print(a.change(amount=500, coins=[1, 2, 5]))  # 12701
