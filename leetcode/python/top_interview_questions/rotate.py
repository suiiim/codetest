from typing import List

"""Given an integer array nums, rotate the array to the right by k steps, where k is non-negative."""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        tmp = nums[-k:]
        for i in range(len(nums) - 1, k - 1, -1):
            nums[i] = nums[i - k]
        for i in range(k):
            nums[i] = tmp[i]

    # Runtime
    def rotate1(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        nums[0:n - k] = reversed(nums[0:n - k])
        nums[n - k:n] = reversed(nums[n - k:n])
        nums[0:n] = reversed(nums[0:n])

    # Memory
    def rotate2(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        nums[:] = nums[n - k:] + nums[:n - k]


if __name__ == '__main__':
    s = Solution()
    s.rotate([1, 2, 3, 4, 5, 6, 7], 3)  # [5,6,7,1,2,3,4]
    s.rotate([-1, -100, 3, 99], 2)  # [3,99,-1,-100]
