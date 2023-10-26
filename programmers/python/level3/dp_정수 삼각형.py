solution = lambda t, l=[]: max(l) if not t else solution(t[1:], [max(x, y) + z for x, y, z in zip([0] + l, l + [0], t[0])])


def solution1(triangle):
    x_max = len(triangle)
    for x in range(-1, -x_max, -1):
        y_max = len(triangle[x])
        for y in range(y_max - 1):
            triangle[x - 1][y] += max(triangle[x][y], triangle[x][y + 1])
    return triangle[0][0]


def solution2(triangle):
    for y, line in enumerate(triangle[1:], start=1):
        for x in range(y + 1):
            if x == 0:
                line[x] += triangle[y - 1][x]
            elif x == y:
                line[x] += triangle[y - 1][x - 1]
            else:
                line[x] += max(triangle[y - 1][x - 1], triangle[y - 1][x])
    return max(triangle[-1])


if __name__ == '__main__':
    print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))  # 30
    print(solution1([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))  # 30
    print(solution2([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))  # 30
