def solution(k, dungeons):
    answer1 = 0
    answer2 = 0
    tmp = k
    # 필요 피로도와 소모피로도의 차이가 큰 순서
    for require, consume in sorted(dungeons, key=lambda x: (-(x[0] - x[1]), x[1])):
        if tmp >= require:
            tmp -= consume
            answer1 += 1
    tmp = k
    # 소모도가 가장 작은 순서
    for require, consume in sorted(dungeons, key=lambda x: (x[1], -(x[0] - x[1]))):
        if tmp >= require:
            tmp -= consume
            answer2 += 1
    return max(answer1, answer2)


if __name__ == '__main__':
    print(solution(80, [[80, 20], [50, 40], [30, 10]]))  # 3
    print(solution(8, [[7, 3], [5, 4], [1, 1]]))  # 3
    print(solution(10, [[9, 2], [10, 3], [7, 3], [5, 4], [1, 1]]))  # 4
    print(solution(40, [[40, 20], [10, 10], [10, 10], [10, 10], [10, 10]]))  # 4
