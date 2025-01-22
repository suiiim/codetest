"""
Given a 0-indexed string s, permute s to get a new string t such that:
All consonants remain in their original places. More formally, if there is an index i with 0 <= i < s.length such that s[i] is a consonant, then t[i] = s[i].
The vowels must be sorted in the nondecreasing order of their ASCII values. More formally,
for pairs of indices i, j with 0 <= i < j < s.length such that s[i] and s[j] are vowels, then t[i] must not have a higher ASCII value than t[j].
Return the resulting string.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in lowercase or uppercase. Consonants comprise all letters that are not vowels.
"""


class Solution:
    # Runtime 113 ms -> 35.73%
    # Memory 20.30 MB -> 50.66%
    def sortVowels(self, s: str) -> str:
        vowels = "aeiou"
        result = ""

        q = sorted(filter(lambda x: x.lower() in vowels, s), reverse=True)

        for i, v in enumerate(s):
            if v.lower() in vowels:
                result += q.pop()
            else:
                result += v

        return ''.join(result)

    # Runtime 28 ms -> 98.49%
    # Memory 18.82 MB -> 96.22%
    def sortVowels2(self, s: str) -> str:
        from collections import Counter
        vowels = "AEIOUaeiou"
        freq = Counter(s)
        vFreq = {vowel: freq[vowel] for vowel in vowels if vowel in freq}

        tab = str.maketrans(vowels, '----------')
        s = s.translate(tab)
        for v in sorted(vFreq.keys()):
            s = s.replace('-', v, vFreq[v])

        return s


a = Solution()
print(a.sortVowels("lEetcOde"))  # "lEOtcede"
print(a.sortVowels("lYmpH"))  # "lYmpH"
