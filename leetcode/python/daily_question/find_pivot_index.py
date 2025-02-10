from typing import List

"""
Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1.
"""


class Solution:
    # Runtime 11 ms -> 33.45%
    # Memory 18.55 MB -> 72.78%
    def pivotIndex(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            dp[i] = nums[i - 1] + dp[i - 1]
        for i in range(len(nums)):
            if dp[i] == dp[-1] - dp[i + 1]:
                return i
        return -1

    # Runtime 6 ms -> 62.61%
    # Memory 18.66 MB -> 50.97%
    def pivotIndex2(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)

        for idx, num in enumerate(nums):
            right -= num
            if left == right:
                return idx
            left += num

        return -1


a = Solution()
print(a.pivotIndex([1, 7, 3, 6, 5, 6]))  # 3
print(a.pivotIndex([1, 2, 3]))  # -1
print(a.pivotIndex([2, 1, -1]))  # 0
