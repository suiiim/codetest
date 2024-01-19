from typing import List

"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
- Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. 
  The remaining elements of nums are not important as well as the size of nums.
- Return k.
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[k]:
                continue
            else:
                k += 1
                nums[k] = nums[i]
        return k


if __name__ == '__main__':
    s = Solution()
    s.removeDuplicates([1, 1, 2])  # [1,2]
    s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])  # [0,1,2,3,4]
