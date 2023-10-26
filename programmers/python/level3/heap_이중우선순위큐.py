def solution(operations):
    answer = []
    for oper in operations:
        o, v = oper.split()
        v = int(v)
        if o == 'I':
            answer.append(v)
        elif answer:
            if v == 1:
                tmp = max(answer)
            else:
                tmp = min(answer)
            answer.remove(tmp)
    return [max(answer), min(answer)] if answer else [0, 0]


if __name__ == '__main__':
    print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))  # [0, 0]
    print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))  # [333, -45]
