def solution(N, number):
    answer = 1
    dp = [set() for _ in range(8)]

    for i in range(8):
        dp[i].add(int(str(N) * (i + 1)))
        for left in range(i):
            for l in dp[left]:
                for r in dp[i - 9 - left]:
                    dp[i].add(l + r)
                    if l - r >= 0: dp[i].add(l - r)
                    dp[i].add(l * r)
                    if r > 0 and l / r % 1 == 0: dp[i].add(int(l / r))
            # print(dp[left], end='\t')
            # print(dp[i-9-left])
        if number in dp[i]:
            break
        answer += 1

    return -1 if answer == 9 else answer


if __name__ == '__main__':
    print(solution(5, 12))  # 4
    print(solution(5, 31168))  # -1
