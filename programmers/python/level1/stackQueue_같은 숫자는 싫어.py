def solution(arr):
    answer = []

    tmp = None
    for a in arr:
        if tmp == a:
            continue
        else:
            answer.append(a)
            tmp = a
    return answer


if __name__ == '__main__':
    print(solution([1, 1, 3, 3, 0, 1, 1]))  # [1, 3, 0, 1]
    print(solution([4, 4, 4, 3, 3]))  # [4, 3]
