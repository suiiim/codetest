from collections import deque


def solution(maps):
    m, n = len(maps[0]), len(maps)
    visit = [[0] * m for _ in range(n)]
    visit[0][0] = 1
    dq = deque([[0, 0]])
    while dq:
        x, y = dq.popleft()
        tmp = visit[x][y] + 1
        for x_, y_ in ([x - 1, y], [x, y - 1], [x + 1, y], [x, y + 1]):
            if 0 <= x_ < n and 0 <= y_ < m and maps[x_][y_] and not visit[x_][y_]:
                visit[x_][y_] = tmp
                dq.append([x_, y_])
    return -1 if not visit[-1][-1] else visit[-1][-1]


if __name__ == '__main__':
    print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))  # 11
    print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))  # -1
