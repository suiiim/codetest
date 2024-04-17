"""
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동
을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다. 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장
빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

5 17
# 2

2 7
# 1

4 6
# 1
"""
import sys

input = sys.stdin.readline


# Memory 36776 KB
# Time 1900 ms
def solution():
    n, k = map(int, input().split())
    if k == n:
        print(0)
        return
    dp = [abs(k - n) + 1] * (n + k + abs(k - n))
    dp[n] = 0

    tmp = [n]
    while tmp:
        x = tmp.pop(0)

        teleport = x * 2
        while 0 < teleport < (n + k + abs(k - n)):
            if dp[x] < dp[x * 2]:
                dp[x * 2] = dp[x]
                tmp.append(x * 2)
            teleport *= 2

        if 0 <= x + 1 <= k and dp[x] + 1 < dp[x + 1]:
            dp[x + 1] = dp[x] + 1
            tmp.append(x + 1)
        if 0 <= x - 1 < (n + k + abs(k - n)) and dp[x] + 1 < dp[x - 1]:
            dp[x - 1] = dp[x] + 1
            tmp.append(x - 1)

    print(dp[k])


# solution()


# Memory 31120 KB
# Time 40 ms
def solution1():
    def dfs(N, K):
        if N >= K: return N - K
        if not N: return 1 + dfs(N + 1, K)
        if not K % 2: return min(K - N, dfs(N, K // 2))
        return 1 + min(dfs(N, K - 1), dfs(N, K + 1))

    N, K = map(int, input().split())
    print(dfs(N, K))


solution1()
