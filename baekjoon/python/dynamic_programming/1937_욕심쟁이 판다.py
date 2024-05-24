"""
n × n의 크기의 대나무 숲이 있다. 욕심쟁이 판다는 어떤 지역에서 대나무를 먹기 시작한다. 그리고 그 곳의 대나무를 다
먹어 치우면 상, 하, 좌, 우 중 한 곳으로 이동을 한다. 그리고 또 그곳에서 대나무를 먹는다. 그런데 단 조건이 있다.
이 판다는 매우 욕심이 많아서 대나무를 먹고 자리를 옮기면 그 옮긴 지역에 그 전 지역보다 대나무가 많이 있어야 한다.
이 판다의 사육사는 이런 판다를 대나무 숲에 풀어 놓아야 하는데, 어떤 지점에 처음에 풀어 놓아야 하고, 어떤 곳으로 이
동을 시켜야 판다가 최대한 많은 칸을 방문할 수 있는지 고민에 빠져 있다. 우리의 임무는 이 사육사를 도와주는 것이다.
n × n 크기의 대나무 숲이 주어져 있을 때, 이 판다가 최대한 많은 칸을 이동하려면 어떤 경로를 통하여 움직여야 하는지 구하여라.

첫째 줄에 대나무 숲의 크기 n(1 ≤ n ≤ 500)이 주어진다. 그리고 둘째 줄부터 n+1번째 줄까지 대나무 숲의 정보가 주어
진다. 대나무 숲의 정보는 공백을 사이로 두고 각 지역의 대나무의 양이 정수 값으로 주어진다. 대나무의 양은 1,000,000
보다 작거나 같은 자연수이다.

첫째 줄에는 판다가 이동할 수 있는 칸의 수의 최댓값을 출력한다.

4
14 9 12 10
1 11 5 4
7 15 2 13
6 3 16 8
# 4
"""
import sys

input = sys.stdin.readline


# Memory 54528 KB
# Time 1000 ms
def solution():
    # 런타임 에러 발생하여 sys.setrecursionlimit(10 ** 6) 사용
    n = int(input())
    forest = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * n for _ in range(n)]
    visit = [[0] * n for _ in range(n)]

    def dfs(a, b, cnt):
        visit[a][b] = 1
        for a_, b_ in ([a + 1, b], [a, b + 1], [a - 1, b], [a, b - 1]):
            if 0 <= a_ < n and 0 <= b_ < n and forest[a][b] < forest[a_][b_]:
                if visit[a_][b_]:
                    dp[a][b] = max(dp[a_][b_] + 1, dp[a][b])
                else:
                    dfs(a_, b_, cnt + 1)
                    dp[a][b] = max(dp[a_][b_] + 1, dp[a][b])

    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                dfs(i, j, 0)

    print(max(map(lambda x: max(x), dp)) + 1)


solution()


# Memory 50840 KB
# Time 572 ms
def solution1():
    n = int(sys.stdin.readline())
    forest = [list(map(int, sys.stdin.readline().strip().split(' ')))
              for _ in range(n)]
    answer = find_out_lasting_days(forest, n)
    print(answer)


def find_out_lasting_days(forest, n):
    memo = [[-1] * n for i in range(n)]
    maximum = 0
    for i in range(n):
        for j in range(n):
            if memo[i][j] == -1:
                memoization(forest, i, j, n, memo)
            if maximum < memo[i][j]:
                maximum = memo[i][j]
    return maximum


def memoization(forest, i, j, n, memo):
    lasting_days_list = []
    if memo[i][j] != -1:
        return memo[i][j]
    if i > 0 and forest[i][j] < forest[i - 1][j]:
        lasting_days_list.append(
            memoization(forest, i - 1, j, n, memo))  # up
    if i < n - 1 and forest[i][j] < forest[i + 1][j]:
        lasting_days_list.append(
            memoization(forest, i + 1, j, n, memo))  # down
    if j > 0 and forest[i][j] < forest[i][j - 1]:
        lasting_days_list.append(
            memoization(forest, i, j - 1, n, memo))  # left
    if j < n - 1 and forest[i][j] < forest[i][j + 1]:
        lasting_days_list.append(memoization(
            forest, i, j + 1, n, memo))  # right
    if not lasting_days_list:
        memo[i][j] = 1
        return 1
    memo[i][j] = max(lasting_days_list) + 1
    return memo[i][j]


solution1()
