from typing import List

"""
You are given a 0-indexed integer array nums. A subarray of nums is called continuous if:
Let i, i + 1, ..., j be the indices in the subarray. Then, for each pair of indices i <= i1, i2 <= j, 0 <= |nums[i1] - nums[i2]| <= 2.
Return the total number of continuous subarrays.
A subarray is a contiguous non-empty sequence of elements within an array.
"""


class Solution:
    # Runtime 905 ms -> 18.01%
    # Memory 27.85 MB -> 33.48%
    def continuousSubarrays(self, nums: List[int]) -> int:
        result = 1
        max_idx, min_idx, cur_idx = 0, 0, 0
        for i in range(1, len(nums)):
            if abs(nums[i - 1] - nums[i]) > 2:
                result += 1
                max_idx, min_idx, cur_idx = i, i, i
                continue
            elif nums[max_idx] <= nums[i]:
                max_idx = i
                if nums[i] - nums[min_idx] > 2:
                    result += i - min_idx
                    cur_idx = min_idx + 1
                    cnt = i - 1
                    while nums[min_idx + 1:i]:
                        if nums[cnt] == min(nums[min_idx + 1:i]):
                            min_idx = cnt
                            break
                        cnt -= 1
                    continue
            if nums[i] <= nums[min_idx]:
                min_idx = i
                if nums[max_idx] - nums[i] > 2:
                    result += i - max_idx
                    cur_idx = max_idx + 1
                    cnt = i - 1
                    while nums[max_idx + 1:i]:
                        if nums[cnt] == max(nums[max_idx + 1:i]):
                            max_idx = cnt
                            break
                        cnt -= 1
                    continue
            result += i - cur_idx + 1

        return result

    def continuousSubarrays2(self, nums: List[int]) -> int:
        from collections import deque
        ans, i, mi, mx = 0, -1, deque(), deque()
        for j, x in enumerate(nums):
            while mi and nums[mi[-1]] >= x: mi.pop()
            mi.append(j)
            while mx and nums[mx[-1]] <= x: mx.pop()
            mx.append(j)
            while nums[mx[0]] - nums[mi[0]] > 2:
                i = min(mi[0], mx[0])
                if mi[0] <= i: mi.popleft()
                if mx[0] <= i: mx.popleft()
            ans += j - i
        return ans


a = Solution()
print(a.continuousSubarrays2([7, 40, 10, 10, 40, 39, 96, 21, 54, 73, 33, 17, 2, 72, 5, 76, 28, 73, 59, 22, 100, 91, 80, 66, 5, 49, 26, 45, 13, 27, 74, 87, 56, 76, 25, 64, 14, 86, 50, 38, 65, 64, 3, 42, 79, 52, 37, 3, 21, 26, 42, 73, 18, 44, 55, 28, 35, 87]))  # 61
print(a.continuousSubarrays2([35, 35, 36, 37, 36, 37, 38, 37, 38]))  # 39
print(a.continuousSubarrays2([42, 41, 42, 41, 41, 40, 39, 38]))  # 28
print(a.continuousSubarrays2([5, 4, 2, 4]))  # 8
print(a.continuousSubarrays2([1, 2, 3]))
