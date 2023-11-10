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


if __name__ == '__main__':
    print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))  # 2
