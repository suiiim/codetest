from collections import deque


def solution(n, computers):
    visited = [False] * (n)
    result = 0

    def dfs(a):
        visited[a] = True
        for i in range(n):
            if not visited[i] and computers[a][i]:
                dfs(i)

    for i in range(n):
        if not visited[i]:
            dfs(i)
            result += 1
    return result


def solution1(n, computers):
    visited = [False] * (n)
    result = 0

    for i in range(n):
        if not visited[i]:
            bfs = deque([i])
            result += 1
            while bfs:
                a = bfs.popleft()
                visited[a] = True
                for b in range(n):
                    if not visited[b] and computers[a][b]:
                        bfs.append(b)

    return result


if __name__ == '__main__':
    print(solution1(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))  # 2
    print(solution1(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))  # 1
