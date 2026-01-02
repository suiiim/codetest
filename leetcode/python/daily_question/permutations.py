from typing import List

"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
"""


class Solution:
    # Runtime 0 ms -> 100%
    # Memory 17.40 MB -> 91.39%
    def permute(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        return list(map(list, permutations(nums, len(nums))))

    # Runtime 0 ms -> 100%
    # Memory 17.54 MB -> 85.31%
    def permute2(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []

        def dfs():
            # base case
            if len(nums) == len(sol):
                res.append(sol.copy())
                return

            # try every number in dif idx
            for num in nums:
                # alr used this num
                if num in sol:
                    continue
                # pick this num
                sol.append(num)
                # go to next position
                dfs()
                # pop to try other nums in that position
                sol.pop()

        dfs()
        return res


a = Solution()
print(a.permute([1, 2, 3]))  # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(a.permute([0, 1]))  # [[0,1],[1,0]]
print(a.permute([1]))  # [[1]]
