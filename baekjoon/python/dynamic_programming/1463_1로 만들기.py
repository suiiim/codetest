
from collections import deque

"""
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다. X가 3으로 나누어 떨어지면, 3으로 나눈다. X가 2로 나누어 떨어지면, 2로 나눈다. 1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

첫째 줄에 1보다 크거나 같고, 10**6보다 작거나 같은 정수 N이 주어진다.

첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
"""


def solution(example_list):
    dp = [float('inf') for _ in range(1000001)]
    x = int(example_list.popleft())
    dp[x] = 0

    for i in range(x, 1, -1):
        if i % 3 == 0:
            dp[int(i / 3)] = min(dp[i] + 1, dp[int(i / 3)])
        if i % 2 == 0:
            dp[int(i / 2)] = min(dp[i] + 1, dp[int(i / 2)])
        dp[int(i - 1)] = min(dp[i] + 1, dp[int(i - 1)])

    print(dp[1])


if __name__ == '__main__':
    solution(deque(['2']))  # 1
    solution(deque(['10']))  # 3
