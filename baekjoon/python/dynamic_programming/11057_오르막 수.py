"""
오르막 수는 수의 자리가 오름차순을 이루는 수를 말한다. 이때, 인접한 수가 같아도 오름차순으로 친다. 예를 들어,
2234와 3678, 11119는 오르막 수이지만, 2232, 3676, 91111은 오르막 수가 아니다. 수의 길이 N이 주어졌을 때,
오르막 수의 개수를 구하는 프로그램을 작성하시오. 수는 0으로 시작할 수 있다.

첫째 줄에 N (1 ≤ N ≤ 1,000)이 주어진다.

첫째 줄에 길이가 N인 오르막 수의 개수를 10,007로 나눈 나머지를 출력한다.

1
# 10

2
# 55

3
# 220
"""
import sys

input = sys.stdin.readline


# Memory 31120 KB
# Time 44 ms
def solution():
    n = int(input())
    dp = [1] * (n + 1)

    for _ in range(9):
        for i in range(1, n + 1):
            dp[i] += dp[i - 1]

    print(dp[-1] % 10007)


solution()


# Memory 30616 KB
# Time 36 ms
def solution1():
    N = int(input())
    ans = 1
    for i in range(1, 10): ans = ans * (N + i) // i
    print(ans % 10007)
