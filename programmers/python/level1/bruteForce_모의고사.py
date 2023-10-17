def solution(answers):
    d = {1: [1, 2, 3, 4, 5], 2: [2, 1, 2, 3, 2, 4, 2, 5], 3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]}
    for k, v in d.items():
        count = 0
        for i, j in enumerate(answers):
            if j == v[i % len(v)]:
                count += 1
        d[k] = count

    high_score = max(d.values())
    d = dict(filter(lambda x: x[1] == high_score, d.items()))

    answer = sorted(d.keys(), key=lambda x: (d[x], - x), reverse=True)
    return answer


def solution1(answers):
    dp = [[0] * len(answers) for _ in range(4)]
    d = {1: [1, 2, 3, 4, 5], 2: [2, 1, 2, 3, 2, 4, 2, 5], 3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]}
    idx = [0] * 4

    for i, a in enumerate(answers, start=1):
        for person in range(1, 4):
            if d[person][idx[person]] == a:
                dp[person][i - 1] = 1
            idx[person] = 0 if i % len(d[person]) == 0 else idx[person] + 1
    result = [sum(rs) for rs in dp]
    return [i for i, j in enumerate(result) if j == max(result)]


if __name__ == '__main__':
    print(solution([1, 2, 3, 4, 5]))  # [1]
    print(solution([1, 3, 2, 4, 2]))  # [1,2,3]
