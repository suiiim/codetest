def solution(routes):
    answer = 0
    a, b = None, None
    for start, end in sorted(routes, key=lambda x: (x[0], -x[1])):
        if a is None and b is None:
            a = start
            b = end
        else:
            a = start
            if a > b:
                answer += 1
                b = end
            else:
                b = min(end, b)

    return answer + 1


def solution1(routes):
    routes = sorted(routes, key=lambda x: x[1])
    last_camera = -30000

    answer = 0

    for route in routes:
        if last_camera < route[0]:
            answer += 1
            last_camera = route[1]

    return answer


def solution2(routes):
    answer = 0
    routes.sort(key=lambda x: x[0], reverse=True)
    camera = 30001
    for route in routes:
        if camera > route[1]:
            answer += 1
            camera = route[0]
    return answer


if __name__ == '__main__':
    print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))  # 2
