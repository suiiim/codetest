"""
Given a string s, find the length of the longest substring without duplicate characters.
"""


class Solution:
    # Runtime 26 ms -> 24.21%
    # Memory 17.84 MB -> 53.07%
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left, right, point = 0, 1, 1
        result = 0

        while right < len(s):
            if s[point] in s[left:right]:
                result = max(result, right - left)
                left += 1
            else:
                right += 1
                point += 1
        return max(result, right - left)

    # Runtime 11 ms -> 95.38%
    # Memory 17.84 MB -> 53.07%
    def lengthOfLongestSubstring2(self, s: str) -> int:
        seen = set()
        l = 0
        longest = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            longest = max(longest, r - l + 1)

        return longest


a = Solution()
print(a.lengthOfLongestSubstring("au"))  # 2
print(a.lengthOfLongestSubstring(" "))  # 1
print(a.lengthOfLongestSubstring("abcabcbb"))  # 3
print(a.lengthOfLongestSubstring("bbbbb"))  # 1
print(a.lengthOfLongestSubstring("pwwkew"))  # 3
