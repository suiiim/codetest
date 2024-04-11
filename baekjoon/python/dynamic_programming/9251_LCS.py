"""
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중
가장 긴 것을 찾는 문제이다. 예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.

ACAYKP
CAPCAK
# 4
"""
import sys

input = sys.stdin.readline


# Memory 56528 KB
# Time 412 ms
def solution():
    s1 = input().strip()
    s2 = input().strip()
    lcs = [[0 for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]

    for i in range(1, len(s2) + 1):
        for j in range(1, len(s1) + 1):
            if s2[i - 1] == s1[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j])

    print(lcs[-1][-1])


# solution()


# Memory 31256 KB
# Time 100 ms
def solution1():
    X = input().rstrip()
    Y = input().rstrip()

    def answer(X, Y):
        DP = [0] * 1000

        for i, x in enumerate(X):
            cnt = 0
            for j, y in enumerate(Y):
                if cnt < DP[j]:
                    cnt = DP[j]
                elif x == y:
                    DP[j] = cnt + 1

        return max(DP)

    print(answer(X, Y))


solution1()
