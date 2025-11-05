from typing import List

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""


class Solution:
    # Runtime 1764 ms -> 22.43%
    # Memory 18.4 MB -> 87.32%
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # Runtime 0 ms -> 100%
    # Memory 19.1 MB -> 10.37%
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            if (target - nums[i]) in seen:
                ans = [seen[target - nums[i]], i]
                return ans
            if nums[i] not in seen:
                seen[nums[i]] = i


a = Solution()
print(a.twoSum(nums=[2, 7, 11, 15], target=9))  # [0,1]
print(a.twoSum(nums=[3, 2, 4], target=6))  # [1,2]
print(a.twoSum(nums=[3, 3], target=6))  # [0,1]
