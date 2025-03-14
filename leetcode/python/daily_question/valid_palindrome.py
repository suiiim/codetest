"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
"""


class Solution:
    # Runtime 11 ms -> 36.25%
    # Memory 18.14 MB -> 58.04%
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left, right = 0, len(s) - 1
        while left < right:
            if not (97 <= ord(s[left]) <= 122 or 48 <= ord(s[left]) <= 57):
                left += 1
            elif not (97 <= ord(s[right]) <= 122 or 48 <= ord(s[right]) <= 57):
                right -= 1
            else:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
        return True

    # Runtime 4 ms -> 90.75%
    # Memory 19.41 MB -> 21.81%
    def isPalindrome2(self, s: str) -> bool:
        import re
        s = re.sub("[^a-z0-9]", "", s.lower())
        if s == s[::-1]:
            return True
        else:
            return False
        # Runtime 7 ms -> 80.73%
        # Memory 19.52 MB -> 20.29%
        # if s:
        #     mid = len(s) // 2
        #     if s[:mid] != s[mid + len(s) % 2:][::-1]:
        #         return False
        # return True

    # Runtime 3 ms -> 98.92%
    # Memory 18.96 MB -> 30.24%
    def isPalindrome3(self, s: str) -> bool:
        temp_str = s.lower()
        temp_str = [letter for letter in temp_str if letter.isalnum()]
        temp_str_reverse = temp_str[::-1]
        if temp_str == temp_str_reverse:
            return True
        else:
            return False


a = Solution()
print(a.isPalindrome("0P"))  # false
print(a.isPalindrome("A man, a plan, a canal: Panama"))  # true
print(a.isPalindrome("race a car"))  # false
print(a.isPalindrome(" "))  # true
