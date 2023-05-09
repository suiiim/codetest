def solution1(k: int, d: int):
    answer = int(d / k) + 1

    x_cnt, y_cnt = 1, 1
    while True:
        if x_cnt > int(d / k):
            break
        x = x_cnt * k
        y_cnt = int(d / k)
        while True:
            y = y_cnt * k
            if x ** 2 + y ** 2 <= d ** 2:
                answer += y_cnt + 1
                x_cnt += 1
                break
            else:
                y_cnt -= 1

    return answer


def solution2(k: int, d: int):
    c = 0
    for y in range(0, d, k):
        x = (d ** 2 - y ** 2) ** 0.5
        c += x // k
    return c + d // k + 1


if __name__ == '__main__':
    print(solution1(2, 4))
    print(solution2(1, 5))
