"""
n가지 종류의 동전이 있다. 이 동전들을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 그러면서 동전의 개수가 최소가
되도록 하려고 한다. 각각의 동전은 몇 개라도 사용할 수 있다.

첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000) 다음 n개의 줄에는 각각의 동전의 가치가 주어진다. 동전의 가치는
100,000보다 작거나 같은 자연수이다. 가치가 같은 동전이 여러 번 주어질 수도 있다.

첫째 줄에 사용한 동전의 최소 개수를 출력한다. 불가능한 경우에는 -1을 출력한다.

3 15
1
5
12
# 3
"""
import sys

input = sys.stdin.readline


# Memory 31120 KB
# Time 356 ms
def solution():
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    coins.sort()
    dp = [0] * (k + 1)

    for i in range(1, k + 1):
        for coin in coins:
            if i < coin:
                break
            if i % coin == 0:
                dp[i] = i // coin
            if dp[i - coin] and dp[i]:
                dp[i] = min(dp[i - coin] + 1, dp[i])
            elif dp[i - coin]:
                dp[i] = dp[i - coin] + 1

    if dp[-1]:
        print(dp[-1])
    else:
        print(-1)


solution()


# Memory 34176 KB
# Time 80 ms
def solution1():
    from collections import deque

    n, k = map(int, input().split())

    # set로 받는 이유는 같은 coin이 들어올 수 있기 때문
    coins = list(i for i in set(int(input()) for _ in range(n)) if i <= k)

    if k in coins:
        print(1)
        exit()

    # deque([(0, 1), (1, 5), (2, 12)])
    que = deque([(i, coin) for i, coin in enumerate(coins)])
    visit = [0] * (k + 1)

    for i in coins:
        visit[i] = 1

    cnt = 1
    while que:
        for _ in range(len(que)):
            index, coin_sum = que.popleft()

            # 왜 시작이 index냐면 5,12 더하는 것과 12,5 더하는 건 같기 때문. 5면 5, 12 더하고 12 면 12만 해주면됨
            # 소수 찾기에서 2*3 이랑 3*2랑 중복되는 부분 피해주는거랑 비슷한 개념
            for i in range(index, len(coins)):
                new_sum = coin_sum + coins[i]
                if new_sum == k:
                    print(cnt + 1)
                    exit(0)
                if new_sum <= k and not visit[new_sum]:
                    que.append((i, new_sum))
                    visit[new_sum] = 1
        cnt += 1

    print(-1)
