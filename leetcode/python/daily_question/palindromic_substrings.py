"""
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.
"""


class Solution:
    # Runtime 778 ms -> 6.65%
    # Memory 17.92 MB -> 34.62%
    def countSubstrings(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] == s[i:j:][::-1]:
                    result += 1
        return result

    # Runtime 91 ms -> 97.96%
    # Memory 17.76 MB -> 65.66%
    def countSubstrings2(self, s: str) -> int:
        left, right = 0, len(s)
        for i in range(right):
            for a, b in [(i, i), (i, i + 1)]:
                while a >= 0 and b < right and s[a] == s[b]:
                    a -= 1
                    b += 1
                left += (b - a) // 2
        return left


a = Solution()
print(a.countSubstrings2("abc"))  # 3
print(a.countSubstrings2("aaa"))  # 6
