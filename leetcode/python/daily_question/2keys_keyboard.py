from typing import List

"""
There is only one character 'A' on the screen of a notepad. You can perform one of two operations on this notepad for each step:
Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.
"""


class Solution:
    # Runtime 0 ms -> 100%
    # Memory 17.90 MB -> 40.83%
    def minSteps(self, n: int) -> int:
        result = 0
        tmp = n
        for i in range(2, n + 1):
            while not tmp % i:
                result += i
                tmp //= i
            if tmp == 1:
                break

        return result


a = Solution()
print(a.minSteps(1))
print(a.minSteps(3))
print(a.minSteps(9))
print(a.minSteps(741))
