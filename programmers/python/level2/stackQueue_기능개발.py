def solution(progresses, speeds):
    answer = []

    ll = list(map(lambda x: (100 - int(x[0])) / int(x[1]), zip(progresses, speeds)))
    ll = list(map(lambda x: int(x) if x == int(x) else int(x) + 1, ll))
    tmp = int()
    num = 1
    print(ll)
    for i in ll:
        if not tmp:
            tmp = i
        else:
            if tmp >= i:
                num += 1
            else:
                answer.append(num)
                tmp = i
                num = 1
    if num:
        answer.append(num)

    return answer


if __name__ == '__main__':
    solution([93, 30, 55], [1, 30, 5])  # [2, 1]
    solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])  # [1, 3, 2]
