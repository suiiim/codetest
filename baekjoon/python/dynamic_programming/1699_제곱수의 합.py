"""
어떤 자연수 N은 그보다 작거나 같은 제곱수들의 합으로 나타낼 수 있다. 예를 들어 11=3^2+1^2+1^2(3개 항)이다. 이런 표현방
법은 여러 가지가 될 수 있는데, 11의 경우 11=2^2+2^2+1^2+1^2+1^2(5개 항)도 가능하다. 이 경우, 수학자 숌크라테스는 “11
은 3개 항의 제곱수 합으로 표현할 수 있다.”라고 말한다. 또한 11은 그보다 적은 항의 제곱수 합으로 표현할 수 없으므로, 11을
그 합으로써 표현할 수 있는 제곱수 항의 최소 개수는 3이다. 주어진 자연수 N을 이렇게 제곱수들의 합으로 표현할 때에 그 항의
최소개수를 구하는 프로그램을 작성하시오.

첫째 줄에 자연수 N이 주어진다. (1 ≤ N ≤ 100,000)

주어진 자연수를 제곱수의 합으로 나타낼 때에 그 제곱수 항의 최소 개수를 출력한다.

7
# 4

12
# 3
"""
import sys

input = sys.stdin.readline


# Memory 31900 KB
# Time 2148 ms
def solution():
    """https://lakelouise.tistory.com/61 너무 어렵다..."""
    n = int(input())

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = i
        for j in range(2, i):
            if (j * j) > i:
                break

            if dp[i - j * j] + 1 < dp[i]:
                dp[i] = dp[i - j * j] + 1

    print(dp[-1])


solution()


# Memory 30616 KB
# Time 36 ms
def solution1():
    N = int(input())

    def sum_of_squares(n):
        while n % 4 == 0 and n > 0:
            n = n // 4
        if n % 8 == 7:
            return 4
        if n - int(n ** 0.5) ** 2 == 0:
            return 1
        for j in range(2, int(n ** (1 / 2)) + 1):
            if n % j == 0:
                factor = [j, 0]
                while n % j == 0:
                    n = n // j
                    factor[1] += 1
                if factor[0] % 4 == 3 and factor[1] % 2 == 1:
                    return 3
        else:
            if n % 4 == 3:
                return 3
        return 2

    print(sum_of_squares(N))


solution1()
