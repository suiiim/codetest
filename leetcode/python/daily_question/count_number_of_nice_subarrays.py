from typing import List

"""
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
Return the number of nice sub-arrays.
"""


class Solution:
    # Runtime 125 ms -> 36.09%
    # Memory 24.01 MB -> 34.83%
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        hash_table = {0: 1}

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1

        total, result = 0, 0
        for i in range(len(nums)):
            total += nums[i]
            if total - k in hash_table:
                result += hash_table[total - k]
            hash_table[total] = hash_table.get(total, 0) + 1

        return result

    def numberOfSubarrays2(self, nums: List[int], k: int) -> int:
        evens = []
        even_count = 0
        for num in nums:
            if num % 2 == 1:
                evens.append(even_count)
                even_count = 0
            else:
                even_count += 1

        evens.append(even_count)

        sol = 0
        for i in range(k, len(evens)):
            sol += (evens[i - k] + 1) * (evens[i] + 1)

        return sol


a = Solution()
print(a.numberOfSubarrays2(nums=[1, 1, 2, 1, 1], k=3))  # 2
print(a.numberOfSubarrays2(nums=[2, 4, 6], k=1))  # 0
print(a.numberOfSubarrays2(nums=[2, 2, 2, 1, 2, 2, 1, 2, 2, 2], k=2))  # 16
