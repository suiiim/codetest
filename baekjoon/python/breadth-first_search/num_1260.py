from collections import deque

"""
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저
방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두
정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
"""


def solution(example_list):
    n, m, v = list(map(int, example_list.popleft().split()))
    point = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for _ in range(m):
        a, b = list(map(int, example_list.popleft().split()))
        point[a][b] = 1
        point[b][a] = 1

    dfs_visit = [False] * (n + 1)
    bfs_visit = [False] * (n + 1)

    def dfs(x):
        result = []
        for i in range(1, n + 1):
            if not dfs_visit[i] and point[x][i]:
                dfs_visit[i] = True
                result.append(i)
                result.extend(dfs(i))
        return result

    dfs_visit[v] = True
    dfs_result = [v, *dfs(v)]
    print(' '.join(map(str, dfs_result)))

    bfs_result = [v]
    bfs_visit[v] = True
    bfs = deque(bfs_result)
    while bfs:
        x = bfs.popleft()
        for i in range(1, n + 1):
            if not bfs_visit[i] and point[x][i]:
                bfs_visit[i] = True
                bfs_result.append(i)
                bfs.append(i)
        if len(bfs_result) == n:
            break
    print(' '.join(map(str, bfs_result)))


def solution1(example_list):
    def dfs(start):
        dfs_visit[start] = True
        print(start, end=' ')
        for i in graph[start]:
            if not dfs_visit[i]:
                dfs(i)

    def bfs(start):
        stack_list = deque([start])
        bfs_visit[start] = True
        print(start, end=' ')
        while stack_list:
            x = stack_list.popleft()
            for i in graph[x]:
                if not bfs_visit[i]:
                    stack_list.append(i)
                    bfs_visit[i] = True
                    print(i, end=' ')

    n, m, v = list(map(int, example_list.popleft().split()))
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = list(map(int, example_list.popleft().split()))
        graph[a].append(b)
        graph[b].append(a)

    for g in graph:
        g.sort()

    dfs_visit = [False] * (n + 1)
    dfs(v)
    print()
    bfs_visit = [False] * (n + 1)
    bfs(v)


if __name__ == '__main__':
    # solution(deque(['4 5 1', '1 2', '1 3', '1 4', '2 4', '3 4']))  # 1 2 4 3 # 1 2 3 4
    # solution(deque(['5 5 3', '5 4', '5 2', '1 2', '3 4', '3 1']))  # 3 1 2 5 4 # 3 1 4 2 5

    solution1(deque(['4 5 1', '1 2', '1 3', '1 4', '2 4', '3 4']))
    solution1(deque(['5 5 3', '5 4', '5 2', '1 2', '3 4', '3 1']))
