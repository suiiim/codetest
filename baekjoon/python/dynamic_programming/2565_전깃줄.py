"""
두 전봇대 A와 B 사이에 하나 둘씩 전깃줄을 추가하다 보니 전깃줄이 서로 교차하는 경우가 발생하였다. 합선의 위험이 있어 이들 중
몇 개의 전깃줄을 없애 전깃줄이 교차하지 않도록 만들려고 한다. 예를 들어, < 그림 1 >과 같이 전깃줄이 연결되어 있는 경우 A의
1번 위치와 B의 8번 위치를 잇는 전깃줄, A의 3번 위치와 B의 9번 위치를 잇는 전깃줄, A의 4번 위치와 B의 1번 위치를 잇는 전깃
줄을 없애면 남아있는 모든 전깃줄이 서로 교차하지 않게 된다. 전깃줄이 전봇대에 연결되는 위치는 전봇대 위에서부터 차례대로 번호
가 매겨진다. 전깃줄의 개수와 전깃줄들이 두 전봇대에 연결되는 위치의 번호가 주어질 때, 남아있는 모든 전깃줄이 서로 교차하지 않
게 하기 위해 없애야 하는 전깃줄의 최소 개수를 구하는 프로그램을 작성하시오.

첫째 줄에는 두 전봇대 사이의 전깃줄의 개수가 주어진다. 전깃줄의 개수는 100 이하의 자연수이다. 둘째 줄부터 한 줄에 하나씩 전깃
줄이 A전봇대와 연결되는 위치의 번호와 B전봇대와 연결되는 위치의 번호가 차례로 주어진다. 위치의 번호는 500 이하의 자연수이고,
같은 위치에 두 개 이상의 전깃줄이 연결될 수 없다.

첫째 줄에 남아있는 모든 전깃줄이 서로 교차하지 않게 하기 위해 없애야 하는 전깃줄의 최소 개수를 출력한다.

8
1 8
3 9
2 2
4 1
6 4
10 10
9 7
7 6
# 3

10
1 6
2 8
3 2
4 9
5 5
6 10
7 4
8 1
9 7
10 3
# 6
"""
import sys

input = sys.stdin.readline


# Memory 31120 KB
# Time 40 ms
def solution():
    n = int(input())
    pole = [list(map(int, input().split())) for _ in range(n)]
    pole = sorted(pole, key=lambda x: x[0])
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if pole[j][1] < pole[i][1]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(n - max(dp))


solution()


# Memory 30616 KB
# Time 36 ms
def solution1():
    a = [0] * 501
    c = [0] * 501
    n = int(input())
    for i in range(n):
        w, x = map(int, sys.stdin.readline().split())
        a[w] = x
    for i in range(501):
        if a[i] != 0:
            c[a[i]] = max(c[:a[i]]) + 1
    print(n - max(c))


solution1()
