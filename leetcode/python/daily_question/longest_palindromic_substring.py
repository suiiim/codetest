from typing import List

"""
Given a string s, return the longest palindromic substring in s.
"""


class Solution:
    # Runtime 658 ms -> 33.75%
    # Memory 17.61 MB -> 88.6%
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

    # Runtime 103 ms -> 96.43%
    # Memory 17.39 MB -> 96.31%
    def longestPalindrome2(self, s: str) -> str:
        length = len(s)
        left, right = 0, 0
        lres = 1
        for i in range(length):
            if (length - i) * 2 + 1 < lres:
                break
            l, r = i, i
            while l > -1 and r < length and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > lres:
                lres = r - l - 1
                left, right = l + 1, r - 1
            l, r = i, i + 1
            while l > -1 and r < length and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > lres:
                lres = r - l - 1
                left, right = l + 1, r - 1
        return s[left: right + 1]

    # Runtime 459 ms -> 37.79%
    # Memory 17.22 MB -> 98.4%
    def longestPalindrome3(self, s: str) -> str:
        if len(s) == 1:
            return s
        elif len(s) == 2:
            return s if s[0] == s[1] else s[0]
        left, right = 0, 0
        for step, extra in ((1, 0), (0, 1)):
            i, j = step, step + extra
            while i < len(s) - 1:
                if s[i] == s[j]:
                    if right - left < j - i:
                        left, right = i, j
                    if 0 <= i - 1 and j + 1 < len(s):
                        i -= 1
                        j += 1
                        continue
                step += 1
                i, j = step, step + extra
        return s[left: right + 1]


a = Solution()
print(a.longestPalindrome("babad"))  # bab
print(a.longestPalindrome("cbbd"))  # bb
print(a.longestPalindrome("a"))  # a
print(a.longestPalindrome("aaaaa"))  # aaaaa
print(a.longestPalindrome("bananas"))  # anana
print(a.longestPalindrome("ac"))  # a
print(a.longestPalindrome("abbcccba"))  # bcccb
