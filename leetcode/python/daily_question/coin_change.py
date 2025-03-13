from typing import List

"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.
"""


class Solution:
    # Runtime 763 ms -> 56.07%
    # Memory 18.2 MB -> 68.92%
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [0] * (amount + 1)
        coins.sort()
        for coin in coins:
            for i in range(amount // coin + 1):
                dp[i * coin] = i

        for i in range(2, amount + 1):
            for coin in coins:
                if i - coin > 0:
                    if dp[i - coin]:
                        if dp[i]:
                            dp[i] = min(dp[i - coin] + 1, dp[i])
                        else:
                            dp[i] = dp[i - coin] + 1

        return dp[-1] if dp[-1] else -1

    # Runtime 702 ms -> 82.86%
    # Memory 17.92 MB -> 97.35%
    def coinChange2(self, coins: List[int], amount: int) -> int:
        # __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


a = Solution()
print(a.coinChange2(coins=[2, 5, 10, 1], amount=27))  # 4
print(a.coinChange2(coins=[1, 2, 5], amount=11))  # 3
print(a.coinChange2(coins=[2], amount=3))  # -1
print(a.coinChange2(coins=[1], amount=0))  # 0
