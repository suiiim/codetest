"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""


class Solution:
    # Runtime 42 ms -> 31.32%
    # Memory 17.8 MB -> 36.43%
    def reverse(self, x: int) -> int:
        if 0 <= x:
            result = int(str(x)[::-1])
        else:
            result = -int(str(abs(x))[::-1])
        return result if -2147483648 <= result <= 2147483647 else 0

    def reverse2(self, x: int) -> int:
        MIN, MAX = -2 ** 31, 2 ** 31 - 1
        negative = False
        if x < 0:
            x = -x
            negative = True
        res = 0
        while x:
            d = x % 10
            x //= 10
            res = res * 10 + d
        if negative:
            res = -res
        if MIN <= res <= MAX:
            return res
        else:
            return 0


a = Solution()
print(a.reverse(123))  # 432
print(a.reverse(-123))  # -321
print(a.reverse(120))  # 21
