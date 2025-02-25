from typing import List

"""
A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and negative.
The first difference (if one exists) may be either positive or negative. A sequence with one element and a sequence with two non-equal elements are trivially wiggle sequences.
For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3) alternate between positive and negative.
In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences. The first is not because its first two differences are positive,
and the second is not because its last difference is zero.
A subsequence is obtained by deleting some elements (possibly zero) from the original sequence, leaving the remaining elements in their original order.
Given an integer array nums, return the length of the longest wiggle subsequence of nums.
"""


class Solution:
    # Runtime 0 ms -> 100%
    # Memory 18.02 MB -> 8.65%
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        prev = nums[0]
        result = 1
        flag = None
        for i in range(1, len(nums)):
            if flag is None:
                if prev < nums[i]:
                    flag = True
                    prev = nums[i]
                elif prev > nums[i]:
                    flag = False
                    prev = nums[i]
                else:
                    continue
            elif flag:
                if prev > nums[i]:
                    flag = not flag
                    prev = nums[i]
                else:
                    prev = max(nums[i], prev)
                    continue
            else:
                if prev < nums[i]:
                    prev = nums[i]
                    flag = not flag
                else:
                    prev = min(nums[i], prev)
                    continue
            result += 1

        return result

    # Runtime 0 ms -> 100%
    # Memory 17.90 MB -> 45.45%
    def wiggleMaxLength2(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0

        up = down = 1

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1

        return max(up, down)


a = Solution()
print(a.wiggleMaxLength([1, 7, 4, 9, 2, 5]))  # 6
print(a.wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]))  # 7
print(a.wiggleMaxLength([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # 2
