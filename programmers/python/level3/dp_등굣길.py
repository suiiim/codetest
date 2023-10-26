def solution(m, n, puddles):
    puddles += [[1, 1]]
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    dp[1][1] = 1
    for x in range(1, n + 1):
        for y in range(1, m + 1):
            if [y, x] in puddles:
                continue
            dp[x][y] = dp[x - 1][y] + dp[x][y - 1]
    return dp[n][m] % 1000000007


if __name__ == '__main__':
    print(solution(4, 3, [[2, 2]]))  # 4
    print(solution(7, 4, [[2, 1], [2, 2], [2, 3], [4, 2], [4, 3], [4, 4], [6, 2], [6, 3]]))  # 0
    print(solution(4, 4, [[3, 2], [2, 4]]))  # 7
    print(solution(100, 100, [[]]))  # 690285631
