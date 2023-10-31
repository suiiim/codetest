def solution(word):
    answer = 0
    dictionary = {'A': 1, 'E': 2, 'I': 3, 'O': 4, 'U': 5}
    num_list = list(map(lambda x: dictionary[x], word)) + [0, 0, 0, 0]
    before_sum = lambda x: sum([(num_list[i] - 1) * 5 ** (x - i) for i in range(min(x, len(word)))])

    for idx, num in enumerate(num_list[:5]):
        answer += before_sum(idx)
        answer += num

    return answer


def solution1(word):
    dict = {'A': 1, 'E': 2, 'I': 3, 'O': 4, 'U': 5}
    n = len(word)
    answer = n
    for i in range(n):
        temp = 0
        for j in range(4 - i, -1, -1):
            temp += 5 ** j
        answer += temp * (dict[word[i]] - 1)
    return answer


def solution2(word):
    # 등비수열 합
    answer = 0
    for i, n in enumerate(word):
        answer += (5 ** (5 - i) - 1) / (5 - 1) * "AEIOU".index(n) + 1
    return answer


if __name__ == '__main__':
    print(solution("AAAAE"))  # 6
    print(solution("AAAE"))  # 10
    print(solution("I"))  # 1563
    print(solution("EIO"))  # 1189
