"""
0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수를 구하는 프로그램을 작성하시오. 덧셈의 순서가 바뀐 경우는
다른 경우로 센다(1+2와 2+1은 서로 다른 경우). 또한 한 개의 수를 여러 번 쓸 수도 있다.

첫째 줄에 두 정수 N(1 ≤ N ≤ 200), K(1 ≤ K ≤ 200)가 주어진다.

첫째 줄에 답을 1,000,000,000으로 나눈 나머지를 출력한다.

20 2
# 21
"""
import sys

input = sys.stdin.readline


# Memory 33164 KB
# Time 148 ms
def solution():
    n, k = map(int, input().split())
    if k == 1:
        print(1)
        return
    dp = [[1] * (n + 1) for _ in range(k - 1)]

    for i in range(1, k - 1):
        for j in range(n + 1):
            dp[i][j] = sum(dp[i - 1][:j + 1])

    print(sum(dp[-1]) % 1000000000)


solution()


# Memory 30616 KB
# Time 36 ms
def solution1():
    def fac(n):
        sum = 1
        for i in range(1, n + 1):
            sum *= i
        return sum

    n, r = map(int, input().split())

    print(fac(n + r - 1) // (fac(r - 1) * fac(n)) % 1000000000)


solution1()
