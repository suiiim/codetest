from typing import List

"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
You have the following three operations permitted on a word:
Insert a character
Delete a character
Replace a character
"""


class Solution:
    # Runtime 61 ms -> 67.17%
    # Memory 23.01 MB -> 8.39%
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            dp[i][0] = i
        for i in range(len(word2) + 1):
            dp[0][i] = i

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[-1][-1]

    # Runtime 13 ms -> 99.72%
    # Memory 22.76 MB -> 8.65%
    def minDistance2(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dists = [[-1] * (n + 1) for _ in range(m + 1)]

        def dp(i, j):
            if dists[i][j] >= 0:
                return dists[i][j]

            if i == 0:
                return j
            if j == 0:
                return i

            if word1[i - 1] == word2[j - 1]:
                result = dp(i - 1, j - 1)
            else:
                result = 1 + min(
                    dp(i - 1, j),  # delete
                    dp(i, j - 1),  # insert
                    dp(i - 1, j - 1)  # replace
                )
            dists[i][j] = result
            return result

        return dp(m, n)

    # Runtime 42 ms -> 84.5%
    # Memory 19.27 MB -> 85.8%
    def minDistance3(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = list(range(m + 1))
        for i in range(1, n + 1):
            ndp = [i]
            c1 = word1[i - 1]
            for j in range(1, m + 1):
                c2 = word2[j - 1]
                ndp.append(min(
                    (0 if c1 == c2 else 1) + dp[j - 1],
                    1 + dp[j],
                    1 + ndp[-1]
                ))
            dp = ndp

        return dp[-1]


a = Solution()
print(a.minDistance3(word1="horse", word2="ros"))  # 3
print(a.minDistance3(word1="intention", word2="execution"))  # 5
