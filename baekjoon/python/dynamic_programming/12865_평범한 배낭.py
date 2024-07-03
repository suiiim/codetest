"""
이 문제는 아주 평범한 배낭에 관한 문제이다. 한 달 후면 국가의 부름을 받게 되는 준서는 여행을 가려고 한다. 세상과의 단절을 
슬퍼하며 최대한 즐기기 위한 여행이기 때문에, 가지고 다닐 배낭 또한 최대한 가치 있게 싸려고 한다. 준서가 여행에 필요하다고 
생각하는 N개의 물건이 있다. 각 물건은 무게 W와 가치 V를 가지는데, 해당 물건을 배낭에 넣어서 가면 준서가 V만큼 즐길 수 있다. 
아직 행군을 해본 적이 없는 준서는 최대 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다. 준서가 최대한 즐거운 여행을 
하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.

첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다. 두 번째 줄부터 N개의 줄에 
거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와 해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다. 입력으로 주어지는 모든 수는 정수이다.

한 줄에 배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력한다.

4 7
6 13
4 8
3 6
5 12
# 14

냅색(Knapsack) 알고리즘
1. Fraction Knapsack: 물건의 가격을 무게로 나누어 무게 대비 가격이 비싼 순서로 물건을 정렬(물건을 자를 수 있음)
2. 0-1 Knapsack: 물건을 자를 수 없기 때문에 물건, 물건의 무게, 배낭의 남은 용량을 고려하여 DP 로 해결
"""
import sys

input = sys.stdin.readline


# Memory 279260 KB
# Time 3084 ms
def solution():
    cnt, weight = map(int, input().split())
    product = [list(map(int, input().split())) for _ in range(cnt)]
    dp = [[0] * (weight + 1) for _ in range(cnt + 1)]

    for i in range(1, cnt + 1):
        w, v = product[i - 1][0], product[i - 1][1]
        for j in range(weight + 1):
            if j < w:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(v + dp[i - 1][j - w], dp[i][j - 1], dp[i - 1][j])

    print(dp[-1][-1])


solution()


# 향상된 DP 풀이
# Memory 34744 KB
# Time 188 ms
def solution1():
    n, k = map(int, input().split())
    k += 1

    bag = {0: 0}
    data = [tuple(map(int, input().split())) for _ in range(n)]
    data.sort(reverse=True)

    for w, v in data:
        tmp = {}
        for v_bag, w_bag in bag.items():
            if bag.get(nv := v + v_bag, k) > (nw := w + w_bag):
                # 새로운 물건을 넣은 가방의 무게보다 최대 무게가 더 크면
                # tmp 딕셔너리에 물건을 넣은 후의 가치 저장
                tmp[nv] = nw
        bag.update(tmp)

    print(max(bag.keys()))


solution1()
