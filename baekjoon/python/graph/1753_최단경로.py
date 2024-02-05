"""
방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 단, 모든 간선의 가중치는 10 이하의 
자연수이다.

첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. (1 ≤ V ≤ 20,000, 1 ≤ E ≤ 300,000) 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 
가정한다. 둘째 줄에는 시작 정점의 번호 K(1 ≤ K ≤ V)가 주어진다. 셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 
순서대로 주어진다. 이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다. u와 v는 서로 다르며 w는 10 이하의 자연수이다. 서로 다른 두 
정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.

첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다. 시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 
경우에는 INF를 출력하면 된다.

5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
# 0 # 2 # 3 # 7 # INF

5 7
1
1 2 1
1 4 4
1 5 10
2 3 1
3 4 1
3 5 1
4 3 5
# 0 # 1 # 2 # 3 # 3

다익스트라(Dijkstra)
- 대표적인 최단 경로(Shartest Path) 탐색 알고리즘
1. 출발 노드 설정
2. 출발 노드 기준으로 각 노드의 최소 비용 저장
3. 방문하지 않은 노드 중 가장 비용이 적은 노드 선택
4. 해당 노드를 거쳐 특정 노드로 가는 경우를 고려하여 최소 비용 갱신
5. 3번에서 4번 과정 반복
"""
import sys
import heapq

input = sys.stdin.readline


# Memory 69652 KB
# Time 212 ms
def solution():
    V, E = map(int, input().split())
    start = int(input())
    path = dict()
    visit = [0] * (V + 1)

    for _ in range(E):
        u, v, w = map(int, input().split())
        if v == start:
            continue
        path.setdefault(u, list()).append([v, w])

    dq = [(0, start)]
    while dq:
        cost, node = dq.pop(0)
        if node in path:
            for next_node, next_cost in path[node]:
                if not visit[next_node] or (visit[node] + next_cost < visit[next_node]):
                    visit[next_node] = visit[node] + next_cost
                    heapq.heappush(dq, (visit[node] + next_cost, next_node))

    for i in range(1, V + 1):
        if i != start and visit[i] == 0:
            print('INF')
        else:
            print(visit[i])


solution()


# MEMORY 84712 KB
# TIME 484 ms
def solution1():
    def dijkstra(start):
        dists[start] = 0
        pq = [(0, start)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dists[u]:
                continue
            for v, w in graph[u]:
                nd = d + w
                if nd < dists[v]:
                    dists[v] = nd
                    heapq.heappush(pq, (nd, v))

    V, E = map(int, sys.stdin.readline().split())
    K = int(sys.stdin.readline())
    graph = [[] for _ in range(V + 1)]
    for line in range(E):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((v, w))

    INF = 1_000_000_000
    dists = [INF] * (V + 1)
    dijkstra(K)

    for d in dists[1:]:
        if d != INF:
            print(d)
        else:
            print('INF')


solution1()
