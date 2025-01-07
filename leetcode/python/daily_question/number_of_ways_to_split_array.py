from typing import List

"""
You are given a 0-indexed integer array nums of length n.
nums contains a valid split at index i if the following are true:
The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
There is at least one element to the right of i. That is, 0 <= i < n - 1.
Return the number of valid splits in nums.
"""


class Solution:
    # Runtime 91 ms -> 16.68%
    # Memory 33.08 MB -> 33.14%
    def waysToSplitArray(self, nums: List[int]) -> int:
        result = 0
        nums_sum = [0] * len(nums)
        nums_sum[0] = nums[0]
        for i in range(1, len(nums)):
            nums_sum[i] = nums_sum[i - 1] + nums[i]

        for i in range(len(nums) - 1):
            if nums_sum[i] >= (nums_sum[-1] - nums_sum[i]):
                result += 1

        return result

    # Runtime 43 ms -> 91.11%
    # Memory 32.3 MB -> 68.81%
    def waysToSplitArray2(self, nums: List[int]) -> int:
        right = sum(nums)
        answer = -1 if right >= 0 else 0
        left = 0
        for num in nums:
            left += num
            right -= num
            if left >= right:
                answer += 1
        return answer


a = Solution()
print(a.waysToSplitArray([10, 4, -8, 7]))
print(a.waysToSplitArray([2, 3, 1, 0]))
