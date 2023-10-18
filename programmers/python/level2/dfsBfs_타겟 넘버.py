def solution(numbers, target):
    value = [-numbers[0], numbers[0]]
    for n in numbers[1:]:
        tmp = []
        for v in value:
            tmp.append(v + n)
            tmp.append(v - n)
        value = tmp
    return value.count(target)


def solution1(numbers, target):
    result = []
    for num in numbers:
        if result:
            tmp = []
            while result:
                r = result.pop()
                tmp.append(r + num)
                tmp.append(r - num)
            result = tmp
        else:
            result.append(num)
            result.append(-num)
    return result.count(target)


if __name__ == '__main__':
    print(solution([1, 1, 1, 1, 1], 3))  # 5
    print(solution([4, 1, 2, 1], 4))  # 2
    print(solution1([1, 1, 1, 1, 1], 3))  # 5
    print(solution1([4, 1, 2, 1], 4))  # 2
