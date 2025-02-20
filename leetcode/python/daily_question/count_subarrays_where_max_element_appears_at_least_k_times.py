from typing import List

"""
You are given an integer array nums and a positive integer k.
Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.
A subarray is a contiguous sequence of elements within an array.
"""


class Solution:
    # Runtime 133 ms -> 16.30%
    # Memory 36.82 MB -> 5.96%
    def countSubarrays(self, nums: List[int], k: int) -> int:
        table = {0: -1}
        num_max = max(nums)
        num = 1
        result = 0

        for i in range(len(nums)):
            if nums[i] == num_max:
                table[num] = i
                num += 1

        for i in range(k, len(table)):
            result += (table[i - k + 1] - table[i - k]) * (len(nums) - table[i])

        return result

    # Runtime 58 ms -> 98.75%
    # Memory 29.63 MB -> 39.66%
    def countSubarrays2(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        cnt = 0
        l = 0
        total = 0

        for num in nums:
            if num == max_num:
                cnt += 1

            while cnt == k:
                if nums[l] == max_num:
                    cnt -= 1
                # outside to keep l going if not max num
                l += 1

            total += l

        return total


a = Solution()
print(a.countSubarrays2(nums=[1, 3, 2, 3, 3], k=2))  # 6
print(a.countSubarrays2(nums=[1, 4, 2, 1], k=3))  # 0
