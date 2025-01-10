from typing import List

"""
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
Since the result may be very large, so you need to return a string instead of an integer.
"""


class Solution:
    # Runtime 0 ms -> 100%
    # Memory 17.88 MB -> 11.46%
    def largestNumber(self, nums: List[int]) -> str:
        nlen = (min(nums) % 10 + 1) * 10  # -> 문자열 비교는 알아서 짧은 단위까지 끊어서 비교
        result = sorted(map(str, nums), key=lambda x: (x * 10)[:nlen])  # 즉, [:nlen] 필요 없음
        if result[0] == "0":
            return "0"
        return str(int(''.join(reversed(result))))


a = Solution()
print(a.largestNumber([111311, 1113]))
print(a.largestNumber([34323, 3432]))
print(a.largestNumber([432, 43243]))
print(a.largestNumber([1]))
print(a.largestNumber([10, 2]))
print(a.largestNumber([3, 30, 34, 5, 9]))
