def solution(number, k):
    total = len(number) - k
    answer = [number[0]]
    for n in number[1:]:
        while answer:
            if int(answer[-1]) < int(n) and k >= 1:
                k -= 1
                answer.pop()
            else:
                break
        answer.append(n)

    return ''.join(answer[:total])


if __name__ == '__main__':
    print(solution("1924", 2))  # "94"
    print(solution("1231234", 3))  # "3234"
    print(solution("4177252841", 4))  # "775841"
    print(solution("121116", 2))  # "2116"
    print(solution("222", 1))  # "22"
