"""
크기가 N×M인 행렬 A와 M×K인 B를 곱할 때 필요한 곱셈 연산의 수는 총 N×M×K번이다. 행렬 N개를 곱하는데 필요한 곱셈 연산
의 수는 행렬을 곱하는 순서에 따라 달라지게 된다. 예를 들어, A의 크기가 5×3이고, B의 크기가 3×2, C의 크기가 2×6인 경우
에 행렬의 곱 ABC를 구하는 경우를 생각해보자. AB를 먼저 곱하고 C를 곱하는 경우 (AB)C에 필요한 곱셈 연산의 수는 5×3×2 +
5×2×6 = 30 + 60 = 90번이다. BC를 먼저 곱하고 A를 곱하는 경우 A(BC)에 필요한 곱셈 연산의 수는 3×2×6 + 5×3×6 = 36
+ 90 = 126번이다. 같은 곱셈이지만, 곱셈을 하는 순서에 따라서 곱셈 연산의 수가 달라진다. 행렬 N개의 크기가 주어졌을 때,
모든 행렬을 곱하는데 필요한 곱셈 연산 횟수의 최솟값을 구하는 프로그램을 작성하시오. 입력으로 주어진 행렬의 순서를 바꾸면 안 된다.

첫째 줄에 행렬의 개수 N(1 ≤ N ≤ 500)이 주어진다. 둘째 줄부터 N개 줄에는 행렬의 크기 r과 c가 주어진다. (1 ≤ r, c ≤ 500)
항상 순서대로 곱셈을 할 수 있는 크기만 입력으로 주어진다.

첫째 줄에 입력으로 주어진 행렬을 곱하는데 필요한 곱셈 연산의 최솟값을 출력한다. 정답은 2^31-1 보다 작거나 같은 자연수이다.
또한, 최악의 순서로 연산해도 연산 횟수가 2^31-1보다 작거나 같다.

3
5 3
3 2
2 6
# 90
"""
import sys

input = sys.stdin.readline


# Memory 113252 KB
# Time 772 ms
def solution():
    # pypy3 로 제출
    n = int(input())
    num = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * n for _ in range(n)]

    for cnt in range(1, n):
        for i in range(0, n - cnt):
            j = i + cnt
            if cnt == 1:
                dp[i][j] = num[i][0] * num[i][1] * num[j][1]
            else:
                dp[i][j] = (2 ** 31) - 1
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + num[i][0] * num[k][1] * num[j][1])

    print(dp[0][-1])


solution()


# Memory 36532 KB
# Time 2428 ms
def main():
    INF = 2 ** 31
    N = int(input())
    f = lambda: tuple(map(int, input().split()))
    num = [*f()] + [f()[1] for _ in range(N - 1)]
    dp = [[0] * N for _ in range(N)]

    for c in range(1, N):  # c: 행렬 개수
        for s in range(N - c):  # s: 시작 인덱스
            t0, e = INF, s + c  # t0: s~e 번째 행렬의 곱셈 연산 수 초기값, e: 마지막 인덱스
            i, j = dp[s][s:e], dp[e][s + 1:e + 1]
            k, ns = num[s] * num[e + 1], num[s + 1:e + 1]
            for m in range(e - s):  # m: 중간 인덱스
                if t0 > (t := i[m] + k * ns[m] + j[m]):
                    t0 = t
            dp[s][e] = dp[e][s] = t0
    print(dp[0][N - 1])


main()


# Memory 117248 KB
# Time 384 ms
def solution1():  # pypy3 확인
    INF = sys.maxsize

    N = int(input())
    m = [[0] * (N + 1) for _ in range(N + 1)]

    p = []
    a, b = map(int, input().split())
    p.append(a)
    p.append(b)
    for i in range(1, N):
        a, b = map(int, input().split())
        p.append(b)

    for i in range(1, N + 1):
        m[i][i] = 0  # 초깃값 셋팅 (i=j인 경우들)

    for i in range(1, N + 1):
        for j in range(i - 1, 0, -1):
            min_value = INF
            for k in range(j, i):
                temp_value = m[j][k] + m[k + 1][i] + p[j - 1] * p[k] * p[i]
                if min_value > temp_value:
                    min_value = temp_value
            m[j][i] = min_value

    print(m[1][N])
