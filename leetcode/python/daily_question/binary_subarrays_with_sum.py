from typing import List

"""
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.
A subarray is a contiguous part of the array.
"""


class Solution:
    # Runtime 3 ms -> 100%
    # Memory 18.58 MB -> 94.31%
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        sums = []
        result = 0

        cnt = 0
        for i in nums:
            if i:
                sums.append(cnt)
                cnt = 0
            else:
                cnt += 1
        sums.append(cnt)

        if goal == 0:
            for i in sums:
                tmp = i
                while tmp:
                    result += tmp
                    tmp -= 1
        else:
            for i in range(goal, len(sums)):
                result += (sums[i - goal] + 1) * (sums[i] + 1)

        return result

    # Runtime 39 ms -> 21.14%
    # Memory 18.54 MB -> 94.31%
    def numSubarraysWithSumk(self, nums, goal):
        left = 0
        right = 0
        cnt = 0
        summ = 0
        if goal < 0:
            return 0

        while right < len(nums):
            summ += nums[right]

            while summ > goal:
                summ -= nums[left]
                left += 1

            cnt += right - left + 1
            right += 1
        return cnt

    def numSubarraysWithSum2(self, nums: List[int], goal: int) -> int:
        return (self.numSubarraysWithSumk(nums, goal) - self.numSubarraysWithSumk(nums, goal - 1))


a = Solution()
print(a.numSubarraysWithSum(nums=[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0], goal=3))  # 48
print(a.numSubarraysWithSum(nums=[1, 0, 1, 0, 1], goal=2))  # 4
print(a.numSubarraysWithSum(nums=[0, 0, 0, 0, 0], goal=0))  # 15
