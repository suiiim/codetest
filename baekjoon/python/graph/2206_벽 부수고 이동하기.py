"""
N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 당신은 (1, 1)에서 (N, M)의 위치까지
이동하려 하는데, 이때 최단 경로로 이동하려 한다. 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.
만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다. 한 칸에서 이동할 수 있는 칸은 상하
좌우로 인접한 칸이다. 맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.

첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.

6 4
0100
1110
1000
0000
0111
0000
# 15

4 4
0111
1111
1111
1110
# -1

5 8
01000000
01010000
01010000
01010011
00010010
# 20

3 3
011
111
110
# -1
"""
import sys
from collections import deque

input = sys.stdin.readline


# Memory 189300 KB
# Time 5868 ms
# 반환 위치 때문에 틀렸음(pop 할 때 확인해야함)
def solution_():
    direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    n, m = map(int, input().split())
    table = [list(map(int, list(input())[:-1])) for _ in range(n)]
    visit = [[[0, 0] for _ in range(m)] for _ in range(n)]
    visit[0][0][0] = 1

    tmp = deque([(0, 0)])
    while tmp:
        x, y = tmp.popleft()
        if x == n - 1 and y == m - 1:
            print(max(visit[x][y]))
            return
        for dx, dy in direction:
            if 0 <= x + dx < n and 0 <= y + dy < m:
                if table[x + dx][y + dy]:  # 이동할 곳이 벽이고
                    if visit[x][y][0]:  # 벽을 뚫지 않은 경로가 있다면 벽을 뚫고 갈 수 있음
                        visit[x + dx][y + dy][1] = visit[x][y][0] + 1
                        tmp.append((x + dx, y + dy))
                else:  # 이동할 곳이 벽이 아니고
                    for i in range(2):
                        if visit[x][y][i] and not visit[x + dx][y + dy][i]:  # 방문하지 않은 곳이라면 갈 수 있음
                            visit[x + dx][y + dy][i] = visit[x][y][i] + 1
                            tmp.append((x + dx, y + dy))

    print(-1)


solution_()


# Memory 188972 KB
# Time 4168 ms
def solution():
    n, m = map(int, input().split())
    table = [list(map(int, input().rstrip())) for _ in range(n)]
    visit = [[[0, 0] for _ in range(m)] for _ in range(n)]
    visit[0][0][0] = 1

    tmp = deque([(0, 0, 0)])
    while tmp:
        x, y, break_f = tmp.popleft()
        if x == n - 1 and y == m - 1:
            print(visit[x][y][break_f])
            return
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            if 0 <= x + dx < n and 0 <= y + dy < m:
                if table[x + dx][y + dy] and not break_f:  # 이동할 곳이 벽이고 벽을 뚫지 않았다면 갈 수 있음
                    visit[x + dx][y + dy][1] = visit[x][y][0] + 1
                    tmp.append((x + dx, y + dy, 1))
                elif not table[x + dx][y + dy] and not visit[x + dx][y + dy][break_f]:  # 이동할 곳이 벽이 아니고 방문하지 않은 곳이라면 갈 수 있음
                    visit[x + dx][y + dy][break_f] = visit[x][y][break_f] + 1
                    tmp.append((x + dx, y + dy, break_f))

    print(-1)


solution()


# Memory 79792 KB
# Time 1848	ms
def solution1():
    n, m = map(int, sys.stdin.readline().split())
    mat = []
    for __ in range(n):
        mat.append(list(sys.stdin.readline()))
    direction = [[1, 0], [-1, 0], [0, -1], [0, 1]]

    queue = deque([[0, 0, 0, 1]])
    visited = [[[False] * m for __ in range(n)] for l in range(2)]
    visited[0][0][0] = True
    visited[1][0][0] = True
    while queue:
        # print(queue)
        y, x, already_break, cnt = queue.popleft()

        if y == n - 1 and x == m - 1:
            # print(y,x,cnt)
            print(cnt)
            return

        for dy, dx in direction:
            ny = dy + y
            nx = dx + x
            if nx < 0 or nx == m or ny < 0 or ny == n:
                continue
            if visited[already_break][ny][nx]:
                continue
            if mat[ny][nx] == '1':
                if already_break:
                    continue
                else:
                    queue.append([ny, nx, 1, cnt + 1])
                    visited[1][ny][nx] = True
                    visited[0][ny][nx] = True
            else:
                queue.append([ny, nx, already_break, cnt + 1])
                visited[already_break][ny][nx] = True
    print(-1)
    return


solution1()
