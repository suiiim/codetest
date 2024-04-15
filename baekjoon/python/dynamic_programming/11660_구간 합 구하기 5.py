"""
N×N개의 수가 N×N 크기의 표에 채워져 있다. (x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램을 작성하시오. (x, y)는 x행 y열을 의미한다.
예를 들어, N = 4이고, 표가 아래와 같이 채워져 있는 경우를 살펴보자. 여기서 (2, 2)부터 (3, 4)까지 합을 구하면 3+4+5+4+5+6 = 27이고,
(4, 4)부터 (4, 4)까지 합을 구하면 7이다. 표에 채워져 있는 수와 합을 구하는 연산이 주어졌을 때, 이를 처리하는 프로그램을 작성하시오.

첫째 줄에 표의 크기 N과 합을 구해야 하는 횟수 M이 주어진다. (1 ≤ N ≤ 1024, 1 ≤ M ≤ 100,000) 둘째 줄부터 N개의 줄에는 표에 채워져
있는 수가 1행부터 차례대로 주어진다. 다음 M개의 줄에는 네 개의 정수 x1, y1, x2, y2 가 주어지며, (x1, y1)부터 (x2, y2)의 합을 구해
출력해야 한다. 표에 채워져 있는 수는 1,000보다 작거나 같은 자연수이다. (x1 ≤ x2, y1 ≤ y2)

총 M줄에 걸쳐 (x1, y1)부터 (x2, y2)까지 합을 구해 출력한다.

4 3
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
2 2 3 4
3 4 3 4
1 1 4 4
# 27
# 6
# 64

2 4
1 2
3 4
1 1 1 1
1 2 1 2
2 1 2 1
2 2 2 2
# 1
# 2
# 3
# 4
"""
import sys

input = sys.stdin.readline


# Memory 106000 KB
# Time 764 ms
def solution():
    n, m = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for x in range(1, n + 1):
        for y in range(1, n + 1):
            dp[x][y] = dp[x - 1][y] + dp[x][y - 1] - dp[x - 1][y - 1] + table[x - 1][y - 1]

    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        if x1 == x2 and y1 == y2:
            print(table[x1 - 1][y1 - 1])
        else:
            print(dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1])


solution()


# Memory 73144 KB
# Time 640 ms
def solve():
    input = sys.stdin.readline
    print = sys.stdout.write
    n, m = map(int, input().split())
    a = [[0] * (n + 1)]
    for _ in range(n):
        a.append([0])
        tmp = 0
        for i, v in enumerate(map(int, input().split()), start=1):
            tmp += v
            a[-1].append(a[-2][i] + tmp)
    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        x1, y1 = x1 - 1, y1 - 1
        print(f'{a[x2][y2] - a[x1][y2] - a[x2][y1] + a[x1][y1]}\n')


solve()
