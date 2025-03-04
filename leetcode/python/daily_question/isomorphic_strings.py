"""
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.
"""


class Solution:
    # Runtime 3 ms -> 96.02%
    # Memory 17.92 MB -> 55.13%
    def isIsomorphic(self, s: str, t: str) -> bool:
        table = {}
        tablei = {}
        for i in range(len(s)):
            if s[i] in table:
                if table[s[i]] == t[i]:
                    continue
                else:
                    return False
            elif t[i] in tablei:
                if tablei[t[i]] == s[i]:
                    continue
                else:
                    return False
            else:
                table[s[i]] = t[i]
                tablei[t[i]] = s[i]
        return True

    # Runtime 3 ms -> 96.02%
    # Memory 17.91 MB -> 55.13%
    def isIsomorphic2(self, s: str, t: str) -> bool:
        final = set(zip(s, t))
        if len(final) == len(set(s)) == len(set(t)):
            return True
        else:
            return False


a = Solution()
print(a.isIsomorphic2(s="badc", t="baba"))  # false
print(a.isIsomorphic2(s="egg", t="add"))  # true
print(a.isIsomorphic2(s="foo", t="bar"))  # false
print(a.isIsomorphic2(s="paper", t="title"))  # true
