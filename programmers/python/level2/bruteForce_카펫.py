def solution(brown, yellow):
    if yellow == 1:
        return [3, 3]

    l = list()
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            l.append(i)
    ll = sorted(l, reverse=True)
    for i, j in zip(l, ll):
        if i >= j:
            if i * 2 + j * 2 + 4 == brown:
                return [i + 2, j + 2]


if __name__ == '__main__':
    print(solution(10, 2))  # [4,3]
    print(solution(8, 1))  # [3,3]
    print(solution(24, 24))  # [8,6]
