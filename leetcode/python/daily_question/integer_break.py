from typing import List

"""
Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.
Return the maximum product you can get.
"""


class Solution:
    # Runtime 0 ms -> 100%
    # Memory 19.46 MB -> 10.59%
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        elif n == 3:
            return 2
        result = 1
        while n:
            if n - 2 == 0:
                return result * 2
            elif n - 3 == 1:
                return result * 4
            else:
                n -= 3
                result *= 3
        return result

    # Runtime 0 ms -> 100%
    # Memory 19.35 MB -> 10.59%
    def integerBreak2(self, n: int) -> int:
        if n <= 3:
            return n - 1
        res = 1
        while n > 4:
            n -= 3
            res *= 3
        return res * n


a = Solution()
print(a.integerBreak(2))  # 1
print(a.integerBreak(10))  # 36
