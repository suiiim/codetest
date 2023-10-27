def solution(s: str):
    tmp = []
    for i in s.split(' '):
        if i:
            tmp.append(''.join([i[0].upper(), i[1:].lower()]))
        else:
            tmp.append(i)

    return ' '.join(tmp)


if __name__ == '__main__':
    print(solution("3peo12951ple unFollowed me"))  # "3people Unfollowed Me"
    print(solution("for the last week"))  # "For The Last Week"
