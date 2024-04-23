"""
n가지 종류의 동전이 있다. 각각의 동전이 나타내는 가치는 다르다. 이 동전을 적당히 사용해서, 그 가치의 합이 k원이
되도록 하고 싶다. 그 경우의 수를 구하시오. 각각의 동전은 몇 개라도 사용할 수 있다. 사용한 동전의 구성이 같은데,
순서만 다른 것은 같은 경우이다.

첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000) 다음 n개의 줄에는 각각의 동전의 가치가 주어진다.
동전의 가치는 100,000보다 작거나 같은 자연수이다.

첫째 줄에 경우의 수를 출력한다. 경우의 수는 2^31보다 작다.

3 10
1
2
5
# 10
"""
import sys

input = sys.stdin.readline


# Memory 31120 KB
# Time 108 ms
def solution():
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    dp = [0] * (k + 1)
    dp[0] = 1

    for c in coins:
        for i in range(c, k + 1):
            dp[i] = dp[i] + dp[i - c]

    print(dp[-1])


solution()
