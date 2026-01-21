from typing import List

"""
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.
"""


class Solution:
    # Runtime 3 ms -> 68.4%
    # Memory 19.38 MB -> 20.78%
    def removeDuplicateLetters(self, s: str) -> str:
        stack = [s[0]]
        for i in range(1, len(s)):
            if s[i] not in stack:
                while stack and s[i] < stack[-1]:
                    if stack[-1] in s[i + 1:]:
                        stack.pop()
                    else:
                        break
                stack.append(s[i])
        return "".join(stack)


a = Solution()
print(a.removeDuplicateLetters("bcabc"))  # "abc"
print(a.removeDuplicateLetters("cbacdcbc"))  # "acdb"
