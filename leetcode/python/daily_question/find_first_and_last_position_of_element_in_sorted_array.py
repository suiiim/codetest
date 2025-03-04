from typing import List

"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
"""


class Solution:
    # Runtime 0 ms -> 100%
    # Memory 19.02 MB -> 53.15%
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target in nums:
            indexes = [i for i, value in enumerate(nums) if value == target]
            return [indexes[0], indexes[-1]]
        else:
            return [-1, -1]

    def searchRange2(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        x = self.fisrtOcc(nums, n, target)
        if (x == -1):
            return [-1, -1]
        y = self.lastOcc(nums, n, target)
        return [x, y]

    def fisrtOcc(self, nums, n, key):
        low = 0
        high = n - 1
        first = -1
        while (low <= high):
            mid = (low + high) // 2
            if (nums[mid] == key):
                first = mid
                high = mid - 1
            elif (nums[mid] < key):
                low = mid + 1
            else:
                high = mid - 1
        return first

    def lastOcc(self, nums, n, key):
        low = 0
        high = n - 1
        last = -1
        while (low <= high):
            mid = (low + high) // 2
            if (nums[mid] == key):
                last = mid
                low = mid + 1
            elif (nums[mid] < key):
                low = mid + 1
            else:
                high = mid - 1
        return last


a = Solution()
print(a.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))  # [3,4]
print(a.searchRange(nums=[5, 7, 7, 8, 8, 10], target=6))  # [-1,-1]
print(a.searchRange(nums=[], target=0))  # [-1,-1]
