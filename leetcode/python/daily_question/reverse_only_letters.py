"""
Given a string s, reverse the string according to the following rules:
All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.
"""


class Solution:
    # Runtime 0 ms -> 100%
    # Memory 17.9 MB -> 33.33%
    def reverseOnlyLetters(self, s: str) -> str:
        tmp = ""
        result = [''] * len(s)

        for i in range(len(s)):
            if 65 <= ord(s[i]) <= 90 or 97 <= ord(s[i]) <= 122:
                tmp += s[i]
            else:
                result[i] = s[i]

        tmp_i = -1
        for i in range(len(result)):
            if not result[i]:
                result[i] = tmp[tmp_i]
                tmp_i -= 1

        return ''.join(result)

    # Runtime 0 ms -> 100%
    # Memory 17.62 MB -> 80.9%
    def reverseOnlyLetters2(self, s: str) -> str:
        l, r = 0, len(s) - 1
        s = list(s)
        while l <= r:
            if not s[r].isalpha():
                r -= 1
            elif not s[l].isalpha():
                l += 1
            else:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return "".join(s)


a = Solution()
print(a.reverseOnlyLetters2("7_28]"))  # "7_28]"
print(a.reverseOnlyLetters2("ab-cd"))  # "dc-ba"
print(a.reverseOnlyLetters2("a-bC-dEf-ghIj"))  # "j-Ih-gfE-dCba"
print(a.reverseOnlyLetters2("Test1ng-Leet=code-Q!"))  # "Qedo1ct-eeLg=ntse-T!"
