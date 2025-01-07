from typing import List

"""
You are given a 0-indexed array of strings words and a 2D array of integers queries.
Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.
Return an array ans of size queries.length, where ans[i] is the answer to the ith query.
"""


class Solution:
    # Runtime 23 ms -> 35.28%
    # Memory 49.82 MB -> 39.57%
    def vowelStrings1(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel = ['a', 'e', 'i', 'o', 'u']
        vowel_cnt = [0] * len(words)
        result = [0] * len(queries)

        for i, w in enumerate(words):
            if w[0] in vowel and w[-1] in vowel:
                vowel_cnt[i] = vowel_cnt[i - 1] + 1
            else:
                vowel_cnt[i] = vowel_cnt[i - 1]

        for i, q in enumerate(queries):
            if q[0] == 0:
                result[i] = vowel_cnt[q[1]]
            else:
                result[i] = vowel_cnt[q[1]] - vowel_cnt[q[0] - 1]

        return result

    # Runtime 21 ms -> 40.91%
    # Memory 49.69 MB -> 72.38%
    def vowelStrings2(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel = {'a', 'e', 'i', 'o', 'u'}
        vowel_cnt = [0] * len(words)
        result = [0] * len(queries)

        for i in range(len(words)):
            if words[i][0] in vowel and words[i][-1] in vowel:
                vowel_cnt[i] = vowel_cnt[i - 1] + 1
            else:
                vowel_cnt[i] = vowel_cnt[i - 1]

        for i in range(len(queries)):
            if queries[i][0] == 0:
                result[i] = vowel_cnt[queries[i][1]]
            else:
                result[i] = vowel_cnt[queries[i][1]] - vowel_cnt[queries[i][0] - 1]

        return result


a = Solution()
print(a.vowelStrings1(["aba", "bcb", "ece", "aa", "e"], [[0, 2], [1, 4], [1, 1]]))
print(a.vowelStrings1(["a", "e", "i"], [[0, 2], [0, 1], [2, 2]]))
