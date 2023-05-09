def solution(line: list):
    answer = []
    intersection = []

    for i in range(len(line) - 1):
        a, b, e = line[i]
        for c, d, f in line[i + 1:]:
            if (a * d - b * c) and not (b * f - e * d) % (a * d - b * c) and (a * d - b * c) and not (e * c - a * f) % (a * d - b * c):
                intersection.append((int((b * f - e * d) / (a * d - b * c)), int((e * c - a * f) / (a * d - b * c))))

    x_max = int(max([i[0] for i in intersection]))
    x_min = int(min([i[0] for i in intersection]))
    y_max = max([i[1] for i in intersection])
    y_min = min([i[1] for i in intersection])

    for y in range(y_max, y_min - 1, -1):
        tmp = ''
        for x in range(x_min, x_max + 1):
            if (x, y) in intersection:
                tmp += '*'
            else:
                tmp += '.'
        answer.append(tmp)

    return answer


def print_solution(result: list):
    for r in result:
        print(r)


if __name__ == '__main__':
    print_solution(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
    print_solution(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
    print_solution(solution([[1, -1, 0], [2, -1, 0]]))
    print_solution(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]))
