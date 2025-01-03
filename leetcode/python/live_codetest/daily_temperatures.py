from typing import List

"""
Given an array of integers temperatures represents the daily temperatures, return an array answer 
such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.
"""


class Solution:
    # Runtime 198 ms -> 5.02%
    # Memory 26.5 MB -> 82.43%
    def dailyTemperatures1(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        high_list = [-1]
        highest = temperatures[-1]
        result = [0] * n

        for ti in range(-2, -(n + 1), -1):
            if temperatures[ti] < highest:
                for hi, idx in enumerate(high_list):
                    if temperatures[ti] < temperatures[idx]:
                        result[ti] = idx - ti
                        high_list = [ti] + high_list[hi:]
                        break
            else:
                high_list = [ti]
                highest = temperatures[ti]

        return result


a = Solution()
print(a.dailyTemperatures1([73, 74, 75, 71, 69, 72, 76, 73]))
print(a.dailyTemperatures1([30, 40, 50, 60]))
print(a.dailyTemperatures1([30, 60, 90]))
