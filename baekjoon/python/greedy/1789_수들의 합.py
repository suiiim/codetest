"""
서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?

첫째 줄에 자연수 S(1 ≤ S ≤ 4,294,967,295)가 주어진다.

첫째 줄에 자연수 N의 최댓값을 출력한다.

200
# 19
"""
import sys

input = sys.stdin.readline


# Memory 31120 KB
# Time 48 ms
def solution():
    s = int(input())
    if s == 1:
        print(1)
    else:
        tmp = 0
        n = 0
        for i in range(1, s):
            tmp += i
            if tmp > s:
                break
            else:
                n += 1
        print(n)


solution()

# Memory 30616 KB
# Time 36 ms
print(int(((1 + int(input()) * 8) ** .5 - 1) / 2))
