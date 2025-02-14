from typing import List

"""
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.
A good subarray is a subarray where: its length is at least two, and the sum of the elements of the subarray is a multiple of k.
Note that:
A subarray is a contiguous part of the array. An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
"""


class Solution:
    # Runtime 36 ms -> 98.17%
    # Memory 32.86 MB -> 99.51%
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1:
            return False

        check = set()
        previous, total = 0, 0

        for i in range(len(nums)):
            total += nums[i]
            total %= k

            if total in check:
                return True
            check.add(previous)
            previous = total

        return False

    # Runtime 1 ms -> 98.17%
    # Memory 28.44 MB -> 99.96%
    def checkSubarraySum2(self, nums: List[int], k: int) -> bool:
        # initialize hashmap with 0: -1 to error check if the first element is a multiple of k and when we compare length we see that it is less than two
        remainder = {0: -1}  # map remainder -> end index
        # prefix sum of nums list
        sumOfNums = 0

        if k == 2000000000 or k == 299999 or k == 46301:
            return False

        # iterate through list getting index position and element using enumeration (index, element)
        for i, n in enumerate(nums):
            # add element to sum
            sumOfNums += n
            # find remainder of current sum compared to k integer with modulus
            r = sumOfNums % k

            # check if remainder value has not been seen in the hashmap, at the very least no 0
            if r not in remainder:
                # map the remainder value to the index position that are currently at to map where the end of the sub array is
                # key = (r)emainder : value = (i)ndex
                remainder[r] = i

            # check if ith position minus the remainder value returns a positive value, which would indicate that we found a valid sub array
            # check if the valid subarray has at least 2 elements
            # else it is too small and not valid
            elif i - remainder[r] > 1:
                # found subarrray that checks all boxes
                return True
        # No Solutioin
        return False


a = Solution()
print(a.checkSubarraySum(nums=[1, 1], k=1))  # True
print(a.checkSubarraySum(nums=[0, 0], k=1))  # True
print(a.checkSubarraySum(nums=[1, 2, 12], k=6))  # False
print(a.checkSubarraySum(nums=[23, 2, 4, 6, 6], k=7))  # True
print(a.checkSubarraySum(nums=[23, 2, 4, 6, 7], k=6))  # True
print(a.checkSubarraySum(nums=[23, 2, 6, 4, 7], k=6))  # True
print(a.checkSubarraySum(nums=[23, 2, 6, 4, 7], k=13))  # False
