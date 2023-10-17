def solution(n, lost, reserve):
    for l in sorted(lost):
        if l in reserve:
            reserve.remove(l)
        elif l - 1 in reserve:
            reserve.remove(l - 1)
        elif l + 1 in reserve and l + 1 not in lost:
            reserve.remove(l + 1)
        else:
            n -= 1

    return n


if __name__ == '__main__':
    print(solution(5, [2, 4], [1, 3, 5]))  # 5
    print(solution(5, [2, 4], [3]))  # 4
