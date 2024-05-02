"""
N×N 크기의 공간에 물고기 M마리와 아기 상어 1마리가 있다. 공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 한 칸에는 물고기가
최대 1마리 존재한다. 아기 상어와 물고기는 모두 크기를 가지고 있고, 이 크기는 자연수이다. 가장 처음에 아기 상어의 크기는 2이고,
아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동한다. 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지
칸은 모두 지나갈 수 있다. 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다. 따라서, 크기가 같은 물고기는 먹을 수 없지만,
그 물고기가 있는 칸은 지나갈 수 있다. 아기 상어가 어디로 이동할지 결정하는 방법은 아래와 같다.
- 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
- 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
- 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
- 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
- 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
- 아기 상어의 이동은 1초 걸리고, 물고기를 먹는데 걸리는 시간은 없다고 가정한다. 즉, 아기 상어가 먹을 수 있는 물고기가 있는 칸으로
  이동했다면, 이동과 동시에 물고기를 먹는다. 물고기를 먹으면, 그 칸은 빈 칸이 된다.
아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다. 예를 들어, 크기가 2인 아기 상어는 물고기를 2마리
먹으면 크기가 3이 된다. 공간의 상태가 주어졌을 때, 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을
수 있는지 구하는 프로그램을 작성하시오.

첫째 줄에 공간의 크기 N(2 ≤ N ≤ 20)이 주어진다. 둘째 줄부터 N개의 줄에 공간의 상태가 주어진다. 공간의 상태는 0, 1, 2, 3, 4,
5, 6, 9로 이루어져 있고, 아래와 같은 의미를 가진다.
0: 빈 칸
1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
9: 아기 상어의 위치
아기 상어는 공간에 한 마리 있다.

첫째 줄에 아기 상어가 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는 시간을 출력한다.

3
0 0 1
0 0 0
0 9 0
# 3

6
5 4 3 2 3 4
4 3 2 3 4 5
3 2 9 5 6 6
2 1 2 3 4 5
3 2 1 6 5 4
6 6 6 6 6 6
# 60
"""
import sys

input = sys.stdin.readline


# Memory 31252 KB
# Time 44 ms
def solution():
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    visit = [[0] * n for _ in range(n)]
    start = [0, 0]
    shark_size = 2
    time = 0
    feed_on = 0

    for x in range(n):
        for y in range(n):
            if graph[x][y] == 9:
                graph[x][y] = 0
                start = [[x, y]]

    cnt = 0
    while start:
        if cnt == 0:
            visit = [[0] * n for _ in range(n)]
        cnt += 1
        tmp = []
        flag = False
        for x, y in start:
            visit[x][y] = 1
            for x_, y_ in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= x_ < n and 0 <= y_ < n and not visit[x_][y_] and graph[x_][y_] <= shark_size:
                    visit[x_][y_] = 1
                    if graph[x_][y_] == shark_size or graph[x_][y_] == 0:
                        # 지나갈 수만 있을 때
                        if not flag:
                            tmp.append([x_, y_])
                    else:
                        # 먹이를 찾았을 때
                        if not flag:
                            tmp = [[x_, y_]]
                        elif x_ < tmp[0][0] or (tmp[0][0] == x_ and y_ < tmp[0][1]):
                            tmp = [[x_, y_]]
                        flag = True

        if flag:
            graph[tmp[0][0]][tmp[0][1]] = 0
            start = tmp
            time += cnt
            cnt = 0
            feed_on += 1
            if feed_on == shark_size:
                feed_on = 0
                shark_size += 1
        else:
            start = list(map(lambda t: [t[0], t[1]], tmp))

    print(time)


solution()


# Memory 30616 KB
# Time 36 ms
def solution1():
    def find_init_pos(N, M):
        for i in range(N):
            for j in range(N):
                if M[i][j] == 9:
                    return i, j

    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def search_prey(N, M, size, current_pos):
        stack, stack_, prey = [current_pos], [], []
        dist = 0
        visited = set()
        while stack and not prey:
            dist += 1
            for (x, y) in stack:
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                for (i, j) in direction:
                    x_, y_ = x + i, y + j
                    if (0 <= x_ < N) and (0 <= y_ < N):
                        if 0 < M[x_][y_] < size:
                            prey.append((x_, y_))
                        elif M[x_][y_] == 0 or M[x_][y_] == size:
                            stack_.append((x_, y_))
            stack = stack_
            stack_ = []
        if prey:
            prey.sort()
            return prey[0], dist
        else:
            return None, 0

    def hunt():
        N = int(input())
        M = [list(map(int, input().split())) for _ in range(N)]
        pos = find_init_pos(N, M)
        M[pos[0]][pos[1]] = 0
        time, size, eat = 0, 2, 0
        while True:
            pos, dist = search_prey(N, M, size, pos)
            if pos is None:
                break
            M[pos[0]][pos[1]] = 0
            time += dist
            eat += 1
            if size == eat:
                size += 1
                eat = 0
        print(time)

    hunt()


solution1()
