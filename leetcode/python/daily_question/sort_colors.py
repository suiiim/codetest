from typing import List

"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue. We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.
"""


class Solution:
    # Runtime 3 ms -> 12.2%
    # Memory 19.34 MB -> 12.01%
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 1
        while i < len(nums):
            j = -1
            while i + j >= 0:
                if nums[i + j + 1] < nums[i + j]:
                    tmp = nums[i + j]
                    nums[i + j] = nums[i + j + 1]
                    nums[i + j + 1] = tmp
                else:
                    break
                j -= 1
            i += 1

    # Runtime 0 ms -> 100%
    # Memory 19.44 MB -> 12.01%
    def sortColors2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, mid, right = 0, 0, len(nums) - 1

        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                mid += 1
                left += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1


a = Solution()
print(a.sortColors([2, 0, 2, 1, 1, 0]))  # [0,0,1,1,2,2]
print(a.sortColors([2, 0, 1]))  # [0,1,2]
