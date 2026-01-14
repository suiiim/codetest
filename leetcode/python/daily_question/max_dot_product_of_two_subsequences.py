from typing import List

"""
Given two arrays nums1 and nums2.

Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.
A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the characters 
without disturbing the relative positions of the remaining characters. (ie, [2,3,5] is a subsequence of [1,2,3,4,5] while [1,5,3] is not).
"""


class Solution:
    # Runtime 145 ms -> 52.77%
    # Memory 21.76 MB -> 79.58%
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[-1000000] * len(nums1) for _ in range(len(nums2))]
        for n in range(len(nums1)):
            dp[0][n] = max(nums1[n] * nums2[0], dp[0][n - 1])
        for n in range(len(nums2)):
            dp[n][0] = max(nums2[n] * nums1[0], dp[n - 1][0])
        for i in range(1, len(nums2)):
            for j in range(1, len(nums1)):
                dp[i][j] = max(nums1[j] * nums2[i], dp[i - 1][j - 1], dp[i - 1][j - 1] + nums1[j] * nums2[i], dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]

    # Runtime 63 ms -> 99.83%
    # Memory 19.39 MB -> 96.99%
    def maxDotProduct2(self, nums1: List[int], nums2: List[int]) -> int:
        l1 = len(nums1)
        l2 = len(nums2)
        maxnum1 = max(nums1)
        minnum2 = min(nums2)
        if maxnum1 < 0 and minnum2 > 0:
            return maxnum1 * minnum2
        minnum1 = min(nums1)
        maxnum2 = max(nums2)
        if minnum1 > 0 and maxnum2 < 0:
            return minnum1 * maxnum2
        prev = [0 for _ in range(l2 + 1)]
        curr = [0 for _ in range(l2 + 1)]
        for i in range(l1):
            indj = 0
            for j in range(1, l2 + 1):
                curr[j] = max(curr[indj], prev[j], nums1[i] * nums2[indj] + prev[indj])
                indj = j
            prev, curr = curr, prev
        return prev[l2]


a = Solution()
print(a.maxDotProduct(nums1=[13, -7, 12, -15, -7, 8, 3, -7, -5, 13, -15, -8, 5, 7, -1, 3, -11, -12, 2, -12], nums2=[-1, 13, -4, -2, -13, 2, -4, 6, -9, 13, -8, -3, -9]))  # 15
print(a.maxDotProduct(nums1=[3, -1, 0], nums2=[4, 5, 3]))  # 15
print(a.maxDotProduct(nums1=[5, -4, -3], nums2=[-4, -3, 0, -4, 2]))  # 28
print(a.maxDotProduct(nums1=[2, 1, -2, 5], nums2=[3, 0, -6]))  # 18
print(a.maxDotProduct(nums1=[3, -2], nums2=[2, -6, 7]))  # 21
print(a.maxDotProduct(nums1=[-1, -1], nums2=[1, 1]))  # -1
