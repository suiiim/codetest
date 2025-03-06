from typing import List

"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
"""


class Solution:
    # Runtime 0 ms -> 100%
    # Memory 18.74 MB -> 45.08%
    def search(self, nums: List[int], target: int) -> int:
        from bisect import bisect_left
        i = bisect_left(nums, target)
        if i < len(nums) and nums[i] == target:
            return i
        else:
            return -1

    # Runtime 0 ms -> 100%
    # Memory 18.91 MB -> 6.38%
    def search2(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                j = m - 1
            else:
                i = m + 1
        return -1


a = Solution()
print(a.search(nums=[-1, 0, 3, 5, 9, 12], target=9))  # 4
print(a.search(nums=[-1, 0, 3, 5, 9, 12], target=2))  # -1
