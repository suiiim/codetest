from typing import List

"""
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) 
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, 
or -1 if it is not in nums. You must write an algorithm with O(log n) runtime complexity.
"""


class Solution:
    # Runtime 0 ms -> 100%
    # Memory 18.15 MB -> 42.3%
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            return -1


a = Solution()
print(a.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))  # 4
print(a.search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))  # -1
print(a.search(nums=[1], target=0))  # -1
