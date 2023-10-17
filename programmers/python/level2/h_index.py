def solution(citations: list):
    answer = int()
    for i in range(len(citations) + 1):
        high = len(list(filter(lambda x: x >= i, citations)))
        low = len(list(filter(lambda x: x <= i, citations)))
        if high >= i >= low:
            answer = i
    return answer


def solution2(citations):
    answer = 0
    citations.sort(reverse=True)

    for i, v in enumerate(citations):
        if v >= citations.__len__() - i and v >= i + 1:
            answer += 1
    return answer


if __name__ == '__main__':
    print(solution([3, 0, 6, 1, 5]))
    print(solution([20, 19, 18, 1]))
