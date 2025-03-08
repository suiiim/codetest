from typing import List

"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. 에이핑크 오하영 강소라
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. 
Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
"""


class Solution:
    # Runtime 0 ms -> 100%
    # Memory 17.6 MB -> 97.98%
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return max(nums)
        dp1 = [0] * len(nums)
        dp2 = [0] * len(nums)
        dp1[0] = nums[0]
        dp1[2] = nums[0] + nums[2]
        dp2[1] = nums[1]
        dp2[2] = nums[2]

        for i in range(3, len(nums)):
            dp1[i] = max(dp1[i - 3], dp1[i - 2]) + nums[i]
            dp2[i] = max(dp2[i - 3], dp2[i - 2]) + nums[i]

        return max(dp1[-2], dp1[-3], dp2[-1], dp2[-2])


a = Solution()
print(a.rob([200, 3, 140, 20, 10]))  # 340
print(a.rob([2, 3, 2]))  # 3
print(a.rob([1, 2, 3, 1]))  # 4
print(a.rob([1, 2, 3]))  # 3
