from typing import List

"""
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.
You should return the array of nums such that the the array follows the given conditions:
1. Every consecutive pair of integers have opposite signs.
2. For all integers with the same sign, the order in which they were present in nums is preserved.
3. The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.
"""


class Solution:
    # Runtime 47 ms -> 64.09%
    # Memory 41.96 MB -> 86.37%
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        pos, neg = 0, 1
        for i in range(len(nums)):
            if nums[i] > 0:
                result[pos] = nums[i]
                pos += 2
            else:
                result[neg] = nums[i]
                neg += 2
        return result


a = Solution()
print(a.rearrangeArray([3, 1, -2, -5, 2, -4]))  # [3,-2,1,-5,2,-4]
print(a.rearrangeArray([-1, 1]))  # [1,-1]
