from typing import List

"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.
"""


class Solution:
    # Runtime 43 ms -> 86.44%
    # Memory 29.16 MB -> 99.69%
    def maxSubArray(self, nums: List[int]) -> int:
        result = max(nums)
        arrange_sums = [result]
        sum_num = 0
        for i in range(len(nums)):
            if 0 < nums[i]:
                sum_num += nums[i]
            else:
                if sum_num and result < sum_num:
                    arrange_sums.append(sum_num)
                if 0 < sum_num + nums[i]:
                    sum_num += nums[i]
                else:
                    sum_num = 0
        if sum_num:
            arrange_sums.append(sum_num)
        return max(arrange_sums)

    # Runtime 15 ms -> 98.03%
    # Memory 29.88 MB -> 95.90%
    def maxSubArray2(self, nums: List[int]) -> int:
        ans = -10 ** 4
        curr = 0
        for x in nums:
            curr += x
            if curr > ans:
                ans = curr
            if curr < 0:
                curr = 0
        return ans


a = Solution()
print(a.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
print(a.maxSubArray([1]))  # 1
print(a.maxSubArray([5, 4, -1, 7, 8]))  # 23
print(a.maxSubArray([-2, -1]))  # -1
print(a.maxSubArray([1, 2, -1, -2, 2, 1, -2, 1, 4, -5, 4]))  # 6
print(a.maxSubArray([1, 1, 1, 1, 1, -10, 4]))  # 5
print(a.maxSubArray([5, -3, 1, -2, 5]))  # 6
