from typing import List

"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
"""


class Solution:
    # Runtime = 85.10 %
    # Memory = 77.94 %
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums), 2):
            if nums[i - 1] != nums[i]:
                return nums[i - 1]
        return nums[-1]

    # Rumtime = 97.87 %
    # Memory = 67.32 %
    def singleNumber1(self, nums: List[int]) -> int:
        xor = 0
        n = len(nums)
        for i in range(n):
            xor = xor ^ nums[i]
        return xor

    # Memory
    def singleNumber2(self, nums: List[int]) -> int:
        nums.sort()
        while True:
            if (nums.count(nums[0]) > 1):
                nums.remove(nums[0])
                nums.remove(nums[0])
            else:
                break
        return nums[0]


if __name__ == '__main__':
    s = Solution()
    s.singleNumber2([2, 2, 1])  # 1
    s.singleNumber2([4, 1, 2, 1, 2])  # 4
    s.singleNumber2([1])  # 1
