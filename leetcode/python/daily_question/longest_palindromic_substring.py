from typing import List

"""
Given a string s, return the longest palindromic substring in s.
"""


class Solution:
    # Runtime 658 ms -> 33.8%
    # Memory 17.61 MB -> 91.26%
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        elif len(s) == 2:
            return s if s[0] == s[1] else s[0]
        result = ""
        for step, extra in ((1, 0), (0, 1)):
            i, j = step, step + extra
            while i < len(s) - 1:
                if s[i] == s[j]:
                    if len(result) < len(s[i:j + 1]):
                        result = s[i:j + 1]
                    if 0 <= i - 1 and j + 1 < len(s):
                        i -= 1
                        j += 1
                        continue
                step += 1
                i, j = step, step + extra
        return result


a = Solution()
print(a.longestPalindrome("babad"))  # bab
print(a.longestPalindrome("cbbd"))  # bb
print(a.longestPalindrome("a"))  # a
print(a.longestPalindrome("aaaaa"))  # aaaaa
print(a.longestPalindrome("bananas"))  # anana
print(a.longestPalindrome("ac"))  # a
print(a.longestPalindrome("abbcccba"))  # bcccb
