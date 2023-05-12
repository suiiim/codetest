def solution(numbers: list):
    a = sorted(map(str, numbers), key=lambda x: x * 10, reverse=True)
    return str(int(''.join(map(str, a))))


if __name__ == '__main__':
    print(solution([6, 10, 2]))
    print(solution([3, 30, 34, 5, 9]))
