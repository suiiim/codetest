"""
춘향이는 편의점 카운터에서 일한다. 손님이 2원짜리와 5원짜리로만 거스름돈을 달라고 한다. 2원짜리 동전과 5원짜리 동전은 무한정 많이
가지고 있다. 동전의 개수가 최소가 되도록 거슬러 주어야 한다. 거스름돈이 n인 경우, 최소 동전의 개수가 몇 개인지 알려주는 프로그램을
작성하시오. 예를 들어, 거스름돈이 15원이면 5원짜리 3개를, 거스름돈이 14원이면 5원짜리 2개와 2원짜리 2개로 총 4개를, 거스름돈이
13원이면 5원짜리 1개와 2원짜리 4개로 총 5개를 주어야 동전의 개수가 최소가 된다.

첫째 줄에 거스름돈 액수 n(1 ≤ n ≤ 100,000)이 주어진다.

거스름돈 동전의 최소 개수를 출력한다. 만약 거슬러 줄 수 없으면 -1을 출력한다.

13
# 5

14
# 4
"""
import sys

input = sys.stdin.readline


# Memory 36264 KB
# Time 56 ms
def solution():
    n = int(input())
    result = [-1] * (n + 1)
    for i in range(1, n + 1):
        if i == 2 or i == 5:
            result[i] = 1
        elif i - 5 > 0 and result[i - 5] != -1:
            result[i] = result[i - 5] + 1
        elif i - 2 > 0 and result[i - 2] != -1:
            result[i] = result[i - 2] + 1
    print(result[n])


solution()


# Memory 30616 KB
# Time 32 ms
def newdana01():
    change = int(input())
    cnt = 0

    while change > 0:
        if change % 5 == 0:
            cnt += change // 5
            change %= 5
            break
        else:
            change -= 2
            cnt += 1

    if change != 0:
        print(-1)
    else:
        print(cnt)


newdana01()
