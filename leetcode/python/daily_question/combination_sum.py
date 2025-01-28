from typing import List

"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates 
where the chosen numbers sum to target. You may return the combinations in any order. The same number may be chosen from candidates 
an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
"""


class Solution:
    # Runtime 2 ms -> 98.46%
    # Memory 17.81 MB -> 43.81%
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if target == 1:
            return []

        dp = [[] for _ in range(target + 1)]

        for num in candidates:
            if num <= target:
                dp[num].append([num])
                for i in range(num + 1, target + 1):
                    if dp[i - num]:
                        for v in dp[i - num]:
                            dp[i].append(v + [num])

        return dp[-1]

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = []

        def help(currSet, currSum, i):
            if currSum == target:
                ans.append(currSet[::])
                return
            elif currSum > target:
                return
            for j in range(i, n):
                currSet.append(candidates[j])
                currSum += candidates[j]
                help(currSet, currSum, j)
                currSum -= candidates[j]
                currSet.pop()

        help([], 0, 0)

        return ans


a = Solution()
print(a.combinationSum2(candidates=[2, 3, 6, 7], target=7))  # [[2,2,3],[7]]
print(a.combinationSum2(candidates=[2, 3, 5], target=8))  # [[2,2,2,2],[2,3,3],[3,5]]
print(a.combinationSum2(candidates=[2], target=1))  # []
