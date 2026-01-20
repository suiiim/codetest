"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character.
You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.
"""


class Solution:
    # Runtime 90 ms -> 84.09%
    # Memory 19.52 MB -> 24.05%
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        max_count = 0
        count = {}
        i, j = 0, 0
        while j < len(s):
            count[s[j]] = count.get(s[j], 0) + 1
            max_count = max(max_count, count[s[j]])
            if j - i + 1 - max_count > k:
                count[s[i]] -= 1
                i += 1
            result = max(result, j - i + 1)
            j += 1
        return result


a = Solution()
print(a.characterReplacement(s="ABAB", k=2))  # 4
print(a.characterReplacement(s="AABABBA", k=1))  # 4
