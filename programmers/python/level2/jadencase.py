def solution(s: str):
    tmp = []
    for i in s.split(' '):
        if i:
            tmp.append(''.join([i[0].upper(), i[1:].lower()]))
        else:
            tmp.append(i)

    return ' '.join(tmp)


if __name__ == '__main__':
    print(solution("3people   unFollowed me"))
    print(solution("for the last week"))
