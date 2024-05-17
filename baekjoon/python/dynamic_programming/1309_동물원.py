"""
어떤 동물원에 가로로 두칸 세로로 N칸인 아래와 같은 우리가 있다. 이 동물원에는 사자들이 살고 있는데 사자들을 우리에 가둘 때,
가로로도 세로로도 붙어 있게 배치할 수는 없다. 이 동물원 조련사는 사자들의 배치 문제 때문에 골머리를 앓고 있다. 동물원 조련
사의 머리가 아프지 않도록 우리가 2*N 배열에 사자를 배치하는 경우의 수가 몇 가지인지를 알아내는 프로그램을 작성해 주도록 하
자. 사자를 한 마리도 배치하지 않는 경우도 하나의 경우의 수로 친다고 가정한다.

첫째 줄에 우리의 크기 N(1≤N≤100,000)이 주어진다.

첫째 줄에 사자를 배치하는 경우의 수를 9901로 나눈 나머지를 출력하여라.

4
# 41
"""
import sys

input = sys.stdin.readline


# Memory 34972 KB
# Time 64 ms
def solution():
    """https://great-park.tistory.com/131"""
    n = int(input())
    if n == 1:
        print(3)
        return

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 3

    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] * 2 + dp[i - 2]) % 9901

    print(dp[-1])


solution()


# Memory 31120 KB
# Time 56 ms
def solution1():
    n = int(input())
    a, b = 1, 3

    for i in range(n - 1):
        a, b = b, (a + b * 2) % 9901

    print(b)


solution1()
