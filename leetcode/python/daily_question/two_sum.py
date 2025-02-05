from typing import List

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""


class Solution:
    # Runtime 0 ms -> 100%
    # Memory 18.89 MB -> 43.42%
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}

        for i in range(len(nums)):
            if target - nums[i] in hash_table:
                return [hash_table[target - nums[i]], i]
            else:
                hash_table.setdefault(nums[i], i)


a = Solution()
print(a.twoSum(nums=[2, 7, 11, 15], target=9))  # [0,1]
print(a.twoSum(nums=[3, 2, 4], target=6))  # [1,2]
print(a.twoSum(nums=[3, 3], target=6))  # [0,1]
