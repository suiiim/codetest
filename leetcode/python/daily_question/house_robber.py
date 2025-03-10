from typing import List

"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and 
it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
"""


class Solution:
    # Runtime 0 ms -> 100%
    # Memory 17.69 MB -> 82.51%
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[2] + nums[0]

        for i in range(3, len(nums)):
            dp[i] = nums[i] + max(dp[i - 2], dp[i - 3])

        return max(dp[-1], dp[-2])


a = Solution()
print(a.rob([1, 2, 3, 1]))  # 4
print(a.rob([2, 7, 9, 3, 1]))  # 12
