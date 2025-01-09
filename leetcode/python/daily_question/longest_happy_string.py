"""
A string s is called happy if it satisfies the following conditions:
s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. 
If there is no such string, return the empty string "". A substring is a contiguous sequence of characters within a string.
"""


class Solution:
    # Runtime 0 ms -> 100%
    # Memory 17.92 MB -> 7.04%
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        from queue import PriorityQueue
        result = ''
        q = PriorityQueue()
        if a:
            q.put((100 - a, 'a'))
        if b:
            q.put((100 - b, 'b'))
        if c:
            q.put((100 - c, 'c'))

        tmp = None
        while q.qsize():
            left, alphabet = q.get()
            if len(result) > 1 and result[-2:] == alphabet * 2:
                tmp = (left, alphabet)
                continue
            while left < 100 and not (len(result) > 1 and result[-2:] == alphabet * 2):
                left += 1
                result += alphabet
                if tmp and (100 - tmp[0]) > (100 - left) * 2:
                    break
            if left < 100:
                q.put((left, alphabet))
            if tmp:
                q.put(tmp)
                tmp = None

        return result

    # Runtime 0 ms -> 100%
    # Memory 17.68 MB -> 24.43%
    def longestDiverseString2(self, a: int, b: int, c: int) -> str:
        import heapq
        res = ""

        heap = []
        if a > 0:
            heapq.heappush(heap, [-a, "a"])
        if b > 0:
            heapq.heappush(heap, [-b, "b"])
        if c > 0:
            heapq.heappush(heap, [-c, "c"])

        while heap:
            val1, char1 = heapq.heappop(heap)

            if len(res) >= 2 and res[-1] == res[-2] == char1:
                if not heap:
                    break

                val2, char2 = heapq.heappop(heap)
                res += char2
                val2 += 1
                if val2:
                    heapq.heappush(heap, [val2, char2])
                heapq.heappush(heap, [val1, char1])
            else:
                res += char1
                val1 += 1
                if val1:
                    heapq.heappush(heap, [val1, char1])

        return res


a = Solution()
# print(a.longestDiverseString(a=1, b=1, c=7))
# print(a.longestDiverseString(a=7, b=1, c=0))
print(a.longestDiverseString(a=0, b=8, c=11))
