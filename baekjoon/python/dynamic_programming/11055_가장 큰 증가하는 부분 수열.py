"""
수열 A가 주어졌을 때, 그 수열의 증가하는 부분 수열 중에서 합이 가장 큰 것을 구하는 프로그램을 작성하시오. 예를 들어, 수열 A
= {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 인 경우에 합이 가장 큰 증가하는 부분 수열은 A = {1, 2, 50, 60} 이고, 합은 113이다.

첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

첫째 줄에 수열 A의 합이 가장 큰 증가하는 부분 수열의 합을 출력한다.

10
1 100 2 50 60 3 5 6 7 8
# 113

5
2 1 5 6 7
# 20

6
100 1 2 3 99
# 105
"""
import sys

input = sys.stdin.readline


# Memory 31120 KB
# Time 112 ms
def solution():
    n = int(input())
    num_list = list(map(int, input().split()))
    dp = [0] * n
    dp[0] = num_list[0]

    for i in range(1, n):
        for j in range(i):
            if num_list[j] < num_list[i]:
                dp[i] = max(dp[j] + num_list[i], dp[i])
        if not dp[i]:
            dp[i] = num_list[i]

    print(max(dp))


# solution()


# Memory 30616 KB
# Time 44 ms
def solution1():
    input()
    dp = [0] * 1001
    for i in map(int, input().split()):
        dp[i] = max(dp[:i]) + i

    print(max(dp))


solution1()
