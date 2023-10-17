def solution(name):
    if not name.strip('A'):
        return 0
    dp = [0] * (len(name))
    for i, n in enumerate(name):
        point = ord(n) - 64
        if point == 1:
            dp[i] = 0
        else:
            dp[i] = min(point - 1, 26 - point + 1)
    rl = min(len(name.rstrip('A')) - 1, len(name[1:].lstrip('A')))
    for c in reversed(range(name.count('A') + 1)):
        right = name.find('A' * c)
        if right != -1 and right != 0 and right + c != len(name):
            left = len(name) - (right + c)
            rl = min(rl, (right - 1) * 2 + left, left * 2 + right - 1)
            break
    return sum(dp) + rl


if __name__ == '__main__':
    print(solution("JEROEN"))  # 56
    print(solution("JAN"))  # 23
    print(solution("ABBBAAAAABB"))  # 12
    print(solution("AAAZZ"))  # 4
    print(solution("ZZZAAAZ"))  # 8
    print(solution("BBAAAAAAAAC"))  # 7
    print(solution("BAAAAAAAA"))  # 1
    print(solution("AAAAA"))  # 0
