"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters
without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""


class Solution:
    # Runtime 0 ms -> 100%
    # Memory 17.8 MB -> 68.06%
    def isSubsequence(self, s: str, t: str) -> bool:
        if s:
            index = 0
            for v in t:
                if v == s[index]:
                    index += 1
                if len(s) == index:
                    return True
            return False
        else:
            return True

    # Runtime 4 ms -> 9.45%
    # Memory 17.49 MB -> 99.9%
    def isSubsequence2(self, s: str, t: str) -> bool:
        i = j = 0

        while i < len(s) and j < len(t):
            if t[j] == s[i]:
                i += 1
                j += 1
            else:
                j += 1

        return i == len(s)


a = Solution()
print(a.isSubsequence2(s="abc", t="ahbgdc"))  # true
print(a.isSubsequence2(s="axc", t="ahbgdc"))  # false
