from typing import List

"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array 
represents your maximum jump length at that position. Return true if you can reach the last index, or false otherwise.
"""


class Solution:
    # Runtime 5105 ms -> 6.78%
    # Memory 28.56 MB -> 5.20%
    def canJump(self, nums: List[int]) -> bool:
        visit = [0] * len(nums)

        def dfs(start, end):
            if not visit[start]:
                visit[start] = 1
                if len(nums) - 1 <= end:
                    return True
                if start < end:
                    for i in range(start + 1, end + 1):
                        if nums[i]:
                            if dfs(i, nums[i] + i):
                                return True
                return False

        return dfs(0, nums[0])

    # Runtime 7030 ms -> 5.00%
    # Memory 18.44 MB -> 77.83%
    def canJump2(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True
        for idx in range(len(nums) - 2, -1, -1):
            dp[idx] = any(dp[idx + step] for step in range(1, nums[idx] + 1) if idx + step < len(nums))
        return dp[0]

    # Runtime 7 ms -> 97.47%
    # Memory 18.60 MB -> 66.12%
    def canJump3(self, nums: List[int]) -> bool:
        # go backwards if we can reach the next element from the current one we are good
        curGoal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= curGoal:
                curGoal = i

        return True if curGoal == 0 else False


a = Solution()
print(a.canJump([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]))  # True
print(a.canJump([1, 2, 3]))  # True
print(a.canJump([2, 3, 1, 1, 4]))  # True
print(a.canJump([3, 2, 1, 0, 4]))  # False
