from typing import List

"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""


class Solution:
    # Runtime 0 ms -> 100%
    # Memory 17.46 MB -> 95.39%
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        queue = [("(", 1, 1)]
        while queue:
            parentheses, pair, cnt = queue.pop()
            if pair == 0:
                if cnt == n:
                    result.append(parentheses)
                else:
                    queue.append((parentheses + "(", pair + 1, cnt + 1))
            else:
                if cnt == n:
                    while pair > 0:
                        parentheses += ")"
                        pair -= 1
                    result.append(parentheses)
                else:
                    queue.append((parentheses + "(", pair + 1, cnt + 1))
                    queue.append((parentheses + ")", pair - 1, cnt))
        return result

    # Runtime 0 ms -> 100%
    # Memory 17.71 MB -> 84.27%
    def generateParenthesis2(self, n: int) -> List[str]:
        res = []

        def dfs(openP, closeP, s):
            if openP == closeP and openP + closeP == n * 2:
                res.append(s)
                return
            if openP < n:
                dfs(openP + 1, closeP, s + "(")
            if closeP < openP:
                dfs(openP, closeP + 1, s + ")")

        dfs(0, 0, "")
        return res


a = Solution()
print(a.generateParenthesis(3))  # ["((()))","(()())","(())()","()(())","()()()"]
print(a.generateParenthesis(1))  # ["()"]
