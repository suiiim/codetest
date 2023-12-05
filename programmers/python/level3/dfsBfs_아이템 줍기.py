def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[0] * 102 for _ in range(102)]
    for r in rectangle:  # 꽉 채운 사각형
        for i in range(r[1] * 2 - 1, r[3] * 2):
            graph[i][r[0] * 2 - 1:r[2] * 2] = [1] * (r[2] * 2 - r[0] * 2 + 1)
    for r in rectangle:  # 속 빈 사각형
        for i in range(r[1] * 2, r[3] * 2 - 1):
            graph[i][r[0] * 2:r[2] * 2 - 1] = [0] * (r[2] * 2 - r[0] * 2 - 1)

    result = [1, 0]  # 총 거리, item 까지 거리

    def dfs(x, y):
        graph[x][y] = 0
        for x_, y_ in [[x + 1, y], [x, y + 1], [x, y - 1], [x - 1, y]]:
            if graph[x_][y_]:
                graph[x_][y_] = 0
                result[0] += 1
                if y_ == itemX * 2 - 1 and x_ == itemY * 2 - 1:
                    result[1] = result[0] - 1
                dfs(x_, y_)
                break

    dfs(characterY * 2 - 1, characterX * 2 - 1)
    return min(int(result[1] / 2), int((result[0] - result[1]) / 2))


if __name__ == '__main__':
    print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))  # 17
    print(solution([[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1))  # 11
    print(solution([[1, 1, 5, 7]], 1, 1, 4, 7))  # 9
    print(solution([[2, 1, 7, 5], [6, 4, 10, 10]], 3, 1, 7, 10))  # 15
    print(solution([[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3))  # 10
