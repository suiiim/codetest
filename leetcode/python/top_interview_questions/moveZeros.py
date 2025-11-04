from typing import List

"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, 1
        while right < len(nums):
            if nums[left]:
                left += 1
                right = left + 1
            else:
                if nums[right]:
                    nums[left] = nums[right]
                    nums[right] = 0
                    left += 1
                right += 1


a = Solution()
print(a.moveZeroes([0, 1, 0, 3, 12]))  # [1,3,12,0,0]
print(a.moveZeroes([0]))  # [0]
