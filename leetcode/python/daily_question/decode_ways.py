"""
You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:
"1" -> 'A' / "2" -> 'B' / ... / "25" -> 'Y' / "26" -> 'Z'
However, while decoding the message, you realize that there are many different ways you can decode the message
because some codes are contained in other codes ("2" and "5" vs "25").
For example, "11106" can be decoded into:
"AAJF" with the grouping (1, 1, 10, 6) / "KJF" with the grouping (11, 10, 6)
The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
Note: there may be strings that are impossible to decode.
Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.
The test cases are generated so that the answer fits in a 32-bit integer.
"""


class Solution:
    # Runtime 1 ms -> 40.88%
    # Memory 17.80 MB -> 52.42%
    def numDecodings(self, s: str) -> int:
        if s[0] == "0" or "00" in s:
            return 0

        dp = [1] * (len(s) + 1)

        for i in range(1, len(s)):
            if s[i - 1] == "0":
                dp[i + 1] = dp[i]
            elif s[i] == "0":
                if int(s[i - 1]) == 0 or 2 < int(s[i - 1]):
                    return 0
                if dp[i] != dp[i - 1]:
                    dp[i + 1] = dp[i - 1]
                else:
                    dp[i + 1] = dp[i]
            elif int(s[i - 1] + s[i]) <= 26:
                dp[i + 1] = dp[i] + dp[i - 1]
            else:
                dp[i + 1] = dp[i]

        return dp[-1]

    # Runtime 0 ms -> 100%
    # Memory 17.68 MB -> 90.25%
    def numDecodings2(self, s: str) -> int:
        dp = [0] * (len(s) + 1)

        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, len(s) + 1):

            if s[i - 1] != '0':
                dp[i] = dp[i - 1]

            two_chars = int(s[i - 2:i])
            if two_chars >= 10 and two_chars <= 26:
                dp[i] += dp[i - 2]

        return dp[len(s)]

    # Runtime 3 ms -> 27.90%
    # Memory 18.03 MB -> 15.61%
    def numDecodings3(self, s: str) -> int:
        if not s or len(s) == 0 or s == '0' or s[0] == '0':
            return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            if '1' <= s[i - 1] <= '9':
                dp[i] += dp[i - 1]
            if '10' <= s[i - 2: i] <= '26':
                dp[i] += dp[i - 2]
        return dp[-1]


a = Solution()
print(a.numDecodings("10011"))  # 0
print(a.numDecodings("2101"))  # 1
print(a.numDecodings("10"))  # 2
print(a.numDecodings("12"))  # 2
print(a.numDecodings("226"))  # 3
print(a.numDecodings("06"))  # 0
