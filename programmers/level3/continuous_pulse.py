def solution(sequence):
    p = 1
    pre1, pre2 = -100000, -100000
    answer = []
    for idx, s in enumerate(sequence):
        s1 = s * p
        s2 = s * -p
        p *= -1
        pre1 = max(s1 + pre1, s1)
        pre2 = max(s2 + pre2, s2)

        answer.append(pre1)
        answer.append(pre2)

    return max(answer)


if __name__ == '__main__':
    print(solution([2, 3, -6, 1, 3, -1, 2, 4]))
    print(solution([234, -435, 4, 1000]))
