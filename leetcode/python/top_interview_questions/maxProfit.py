from typing import List

"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. 
However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 10 ** 4
        answer = 0
        for price in prices:
            if buy < price:
                answer += price - buy
                buy = price
            else:
                buy = price
        return answer

    # Memory
    def maxProfit1(self, prices: List[int]) -> int:
        j = 1
        max_profit = 0
        while (j < len(prices)):
            profit = prices[j] - prices[j - 1]
            if profit > 0:
                max_profit += profit
            j += 1
        return max_profit


if __name__ == '__main__':
    s = Solution()
    s.maxProfit([7, 1, 5, 3, 6, 4])  # 7
    s.maxProfit([1, 2, 3, 4, 5])  # 4
    s.maxProfit([7, 6, 4, 3, 1])  # 0
