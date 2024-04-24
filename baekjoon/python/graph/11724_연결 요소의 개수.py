"""
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에
간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

첫째 줄에 연결 요소의 개수를 출력한다.

6 5
1 2
2 5
5 1
3 4
4 6
# 2

6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
# 1
"""
import sys

input = sys.stdin.readline


# Memory 38460 KB
# Time 712 ms
def solution():
    # 런타임 에러 발생하여 sys.setrecursionlimit(100000) 사용
    n, m = map(int, input().split())
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    visit = [0] * (n + 1)
    result = 0

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u][v] = 1
        graph[v][u] = 1

    def dfs(num):
        visit[num] = 1
        for next_num, _ in filter(lambda x: x[1], enumerate(graph[num])):
            if not visit[next_num]:
                dfs(next_num)

    for i in range(1, n + 1):
        tmp = sum(visit)
        dfs(i)
        if tmp != sum(visit):
            result += 1

    print(result)


# solution()


# Memory 31256 KB
# Time 52 ms
def solution1():
    N, M = map(int, sys.stdin.readline().split())
    c, t = N, 1
    li = [0 for _ in range(N + 1)]
    for _ in range(M):
        if c == 1: break
        i, j = map(int, sys.stdin.readline().split())
        if li[i] * li[j] == 0:
            if li[i] == li[j]:
                li[i] = li[j] = t
                t += 1
            else:
                li[i] = li[j] = li[i] + li[j]
        elif li[i] != li[j]:
            s = min(li[i], li[j])
            l = max(li[i], li[j])
            for k in range(1, N + 1):
                if li[k] == l:
                    li[k] = s
        else:
            c += 1
        c -= 1
    print(c)


solution1()
