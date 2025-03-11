from typing import List

"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


class Solution:
    # Runtime 13 ms -> 99.14%
    # Memory 26.94 MB -> 33.22%
    def maxProfit(self, prices: List[int]) -> int:
        high = 0
        low = 10 ** 4
        result = 0

        for v in reversed(prices):
            if high < v:
                high = v
                low = v
            else:
                if v < low:
                    low = v
                    result = max(result, high - low)
        return result

    # Runtime 1102 ms -> 5%
    # Memory 25 MB -> 99.91%
    def maxProfit2(self, prices: List[int]) -> int:
        profit = 0

        while len(prices) > 1:
            buy = min(prices)
            sell = max(prices[prices.index(buy):])

            if sell - buy > profit:
                profit = sell - buy
            del prices[prices.index(buy):]
        return profit


a = Solution()
print(a.maxProfit2([7, 1, 5, 3, 6, 4]))  # 5
print(a.maxProfit2([7, 6, 4, 3, 1]))  # 0
