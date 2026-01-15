from typing import List

"""
Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.
"""


class Solution:
    # Runtime 582 ms -> 18.23%
    # Memory 76.17 MB -> 14.92%
    def tupleSameProduct(self, nums: List[int]) -> int:
        result = 0
        h = {}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                h.setdefault(nums[i] * nums[j], []).extend((nums[i], nums[j]))
        for k, v in h.items():
            if len(v) > 2:
                result += len(v) * (len(v) - 2)
        return result

    # Runtime 323 ms -> 88.4%
    # Memory 48.47 MB -> 17.68%
    def tupleSameProduct2(self, nums: List[int]) -> int:
        from collections import Counter
        from itertools import combinations
        seen = Counter(i * j for i, j in combinations(nums, 2))
        return sum(4 * i * (i - 1) for i in seen.values() if i >= 2)

    # Runtime 280 ms -> 96.13%
    # Memory 48.19 MB -> 21.55%
    def tupleSameProduct3(self, nums: List[int]) -> int:
        n = len(nums)
        prod_to_appear = {}
        for i in range(n - 1):
            for j in range(i + 1, n):
                key = nums[i] * nums[j]
                prod_to_appear[key] = prod_to_appear.get(key, 0) + 1
        res = 0
        for k in prod_to_appear.values():
            if k >= 2:
                res += (k * (k - 1) // 2) * 8
        return res


a = Solution()
print(a.tupleSameProduct([2, 3, 4, 6]))  # 8
print(a.tupleSameProduct([1, 2, 4, 5, 10]))  # 16
