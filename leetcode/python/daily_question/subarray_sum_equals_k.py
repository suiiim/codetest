from typing import List

"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.
"""


class Solution:
    # Runtime 43 ms -> 21.32%
    # Memory 20.37 MB -> 65.87%
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_table = {}
        total = 0
        result = 0
        for i in range(len(nums)):
            total += nums[i]
            if total == k:
                result += 1
            if total - k in hash_table:
                result += hash_table[total - k]
            hash_table.setdefault(total, 0)
            hash_table[total] += 1

        return result

    # Runtime 31 ms -> 62.15%
    # Memory 20.37 MB -> 65.87%
    def subarraySum2(self, nums: List[int], k: int) -> int:
        sub_num = {0: 1}
        total = count = 0

        for n in nums:
            total += n

            if total - k in sub_num:
                count += sub_num[total - k]

            sub_num[total] = 1 + sub_num.get(total, 0)

        return count


a = Solution()
print(a.subarraySum2(nums=[1, -1, 0], k=0))  # 3
print(a.subarraySum2(nums=[100, 1, 2, 3, 4], k=6))  # 1
print(a.subarraySum2(nums=[1, 1, 1], k=2))  # 2
print(a.subarraySum2(nums=[1, 2, 3], k=3))  # 2
