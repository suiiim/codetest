def solution(money):
    if len(money) == 3:
        return max(money)

    dp1 = [0] * len(money)  # 첫번째집 털기
    dp2 = [0] * len(money)  # 첫번째집 안 털기
    dp1[0] = money[0]
    dp1[2] = money[0] + money[2]
    dp2[1] = money[1]

    for i in range(2, len(money)):
        if i == len(money) - 1:
            dp1[i] = max(dp1[i - 3], dp1[i - 2], dp1[i - 1])
            dp2[i] = max(dp2[i - 3] + money[i], dp2[i - 2] + money[i], dp2[i - 1])
        else:
            dp1[i] = max(dp1[i - 3] + money[i], dp1[i - 2] + money[i], dp1[i - 1])
            dp2[i] = max(dp2[i - 3] + money[i], dp2[i - 2] + money[i], dp2[i - 1])

    return max(dp1[-1], dp1[-2], dp2[-1], dp2[-2])


def solution1(a):
    x1, y1, z1 = a[0], a[1], a[0] + a[2]
    x2, y2, z2 = 0, a[1], a[2]
    for i in a[3:]:
        x1, y1, z1 = y1, z1, max(x1, y1) + i
        x2, y2, z2 = y2, z2, max(x2, y2) + i
    return max(x1, y1, y2, z2)  # z1 제외 가장 큰값


if __name__ == '__main__':
    # print(solution([1, 2, 3, 1]))  # 4
    # print(solution([1, 1, 8]))  # 8
    # print(solution([30, 50, 10, 40, 70]))  # 120
    # print(solution([1, 100, 1, 100, 1]))  # 200
    # print(solution([1, 2, 3, 1, 5]))  # 8

    print(solution1([1, 2, 3, 1]))  # 4
    print(solution1([1, 1, 8]))  # 8
    print(solution1([30, 50, 10, 40, 70]))  # 120
    print(solution1([1, 100, 1, 100, 1]))  # 200
    print(solution1([1, 2, 3, 1, 5]))  # 8
