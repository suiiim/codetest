"""
0과 1로만 이루어진 수를 이진수라 한다. 이러한 이진수 중 특별한 성질을 갖는 것들이 있는데, 이들을 이친수(pinary number)라 한다. 이친수는 다음의 성질을 만족한다.
1. 이친수는 0으로 시작하지 않는다.
2. 이친수에서는 1이 두 번 연속으로 나타나지 않는다. 즉, 11을 부분 문자열로 갖지 않는다.
예를 들면 1, 10, 100, 101, 1000, 1001 등이 이친수가 된다. 하지만 0010101이나 101101은 각각 1, 2번 규칙에 위배되므로 이친수가 아니다.
N(1 ≤ N ≤ 90)이 주어졌을 때, N자리 이친수의 개수를 구하는 프로그램을 작성하시오.

첫째 줄에 N이 주어진다.

첫째 줄에 N자리 이친수의 개수를 출력한다.

3
# 2
"""
import sys

input = sys.stdin.readline


# Memory 31120 KB
# Time 40 ms
def solution():
    n = int(input())
    if n == 1:
        print(1)
        return
    dp = [1] * n

    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]

    print(dp[-1])


solution()


# Memory 30616 KB
# Time 32 ms
def solution1():
    n = int(input())

    arr = [[0, 0] for i in range(91)]

    arr[1][1] = 1  # 1

    for i in range(2, n + 1):
        arr[i][0] = arr[i - 1][0] + arr[i - 1][1]  # 피보나치처럼 되네
        arr[i][1] = arr[i - 1][0]

    print(sum(arr[n]))
