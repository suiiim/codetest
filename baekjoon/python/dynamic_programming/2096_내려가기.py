"""
N줄에 0 이상 9 이하의 숫자가 세 개씩 적혀 있다. 내려가기 게임을 하고 있는데, 이 게임은 첫 줄에서 시작해서 마지막 줄에서 끝나
게 되는 놀이이다. 먼저 처음에 적혀 있는 세 개의 숫자 중에서 하나를 골라서 시작하게 된다. 그리고 다음 줄로 내려가는데, 다음 줄
로 내려갈 때에는 다음과 같은 제약 조건이 있다. 바로 아래의 수로 넘어가거나, 아니면 바로 아래의 수와 붙어 있는 수로만 이동할 수
있다는 것이다. 이 제약 조건을 그림으로 나타내어 보면 다음과 같다. 별표는 현재 위치이고, 그 아랫 줄의 파란 동그라미는 원룡이가
다음 줄로 내려갈 수 있는 위치이며, 빨간 가위표는 원룡이가 내려갈 수 없는 위치가 된다. 숫자표가 주어져 있을 때, 얻을 수 있는 최
대 점수, 최소 점수를 구하는 프로그램을 작성하시오. 점수는 원룡이가 위치한 곳의 수의 합이다.

첫째 줄에 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에는 숫자가 세 개씩 주어진다. 숫자는 0, 1, 2, 3, 4, 5, 6, 7, 8,
9 중의 하나가 된다.

첫째 줄에 얻을 수 있는 최대 점수와 최소 점수를 띄어서 출력한다.

3
1 2 3
4 5 6
4 9 0
# 18 6

3
0 0 0
0 0 0
0 0 0
# 0 0
"""
import sys

input = sys.stdin.readline


# Memory 31120 KB
# Time 284 ms
def solution():
    n = int(input())
    dp_min, dp_max = [0, 0, 0], [0, 0, 0]

    for i in range(n):
        a, b, c = map(int, input().split())
        dp_min = [min(dp_min[:2]) + a, min(dp_min[:]) + b, min(dp_min[1:]) + c]
        dp_max = [max(dp_max[:2]) + a, max(dp_max[:]) + b, max(dp_max[1:]) + c]

    print(max(dp_max), min(dp_min))


solution()


# Memory 31120 KB
# Time 168 ms
def solution1():
    N = int(input())
    max1, max2, max3 = map(int, input().split())
    min1, min2, min3 = max1, max2, max3
    for row in range(1, N):
        tmp1, tmp2, tmp3 = map(int, input().split())
        if max1 > max2:
            if max2 > max3:
                max1, max2, max3 = tmp1 + max1, tmp2 + max1, tmp3 + max2
            else:
                if max1 > max3:
                    max1, max2, max3 = tmp1 + max1, tmp2 + max1, tmp3 + max3
                else:
                    max1, max2, max3 = tmp1 + max1, tmp2 + max3, tmp3 + max3
        else:
            if max2 > max3:
                max1, max2, max3 = tmp1 + max2, tmp2 + max2, tmp3 + max2
            else:
                max1, max2, max3 = tmp1 + max2, tmp2 + max3, tmp3 + max3

        if min1 > min2:
            if min2 > min3:
                min1, min2, min3 = tmp1 + min2, tmp2 + min3, tmp3 + min3
            else:
                min1, min2, min3 = tmp1 + min2, tmp2 + min2, tmp3 + min2
        else:
            if min2 > min3:
                if min1 > min3:
                    min1, min2, min3 = tmp1 + min1, tmp2 + min3, tmp3 + min3
                else:
                    min1, min2, min3 = tmp1 + min1, tmp2 + min1, tmp3 + min3
            else:
                min1, min2, min3 = tmp1 + min1, tmp2 + min1, tmp3 + min2

    print(max([max1, max2, max3]), min([min1, min2, min3]))


solution1()
