from typing import List

"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
"""


class Solution:
    # Runtime 11 ms -> 83.07%
    # Memory 22.15 MB -> 29.05%
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter
        counter = Counter(strs)
        duplicates_with_count = {item: count for item, count in counter.items() if count > 1}
        anagram_hash = {s: ''.join(sorted(s)) for s in strs}
        rs = {}
        for k, v in anagram_hash.items():
            rs.setdefault(v, []).extend([k] * duplicates_with_count.get(k, 1))
        return list(rs.values())

    # Runtime 11 ms -> 83.07%
    # Memory 22.1 MB -> 29.05%
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for word in strs:
            key = tuple(sorted(word))
            if key not in result:
                result[key] = []
            result[key].append(word)

        return list(result.values())


a = Solution()
print(a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  # [["bat"],["nat","tan"],["ate","eat","tea"]]
print(a.groupAnagrams([""]))  # [[""]]
print(a.groupAnagrams(["a"]))  # [["a"]]
print(a.groupAnagrams(["tea", "", "eat", "", "tea", ""]))  # [["","",""],["eat","tea","tea"]]
